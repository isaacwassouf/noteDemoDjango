from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

# Create your views here.

def index(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/posts')



def posts(request):
    if request.user.is_authenticated:
        uid=request.user.id
        posts=Post.objects.filter(user=uid)
        context={
            'posts':posts,
        }
        return render(request,'posts/index.html',context)
    else:
        return HttpResponse("User is not looged in")


def item(request,id):
    if request.user.is_authenticated:
        # uid=request.user.id
        post= Post.objects.get(id=id)
        context={
            'post': post
        }
        # print(request.user.id)
        return render(request,'posts/item.html',context)
    else:
        return HttpResponse("User is not logged in")

def modify(request,id):
    if request.user.is_authenticated:
        if (request.method=='GET'):
            post=Post.objects.get(id=id)
            context={
            'post':post
            }
            return render(request,'posts/modify.html',context)

        else:
            title=request.POST['title']
            content=request.POST['content']

            post=Post.objects.get(id=id)
            post.title=title
            post.content=content
            post.save()
            return redirect('/posts')
    else:
        return HttpResponse("User is not logged in")


def add(request):
    if request.user.is_authenticated:
        if(request.method =='GET'):
            title=request.GET['title']
            context={
                'title':title,
            }
            return render(request,'posts/add.html',context)

        else:
            title=request.POST['title']
            content=request.POST['content']

            uid=request.user.id
            user= User.objects.get(id=uid)
            newPost=Post( title=title,content=content,user=user)
            newPost.save()
            return redirect('/posts')
    else:
        return HttpResponse("User is not looged in")

def home(request):
    if(request.method=='GET'):
        return render(request,'posts/login.html')


def signup(request):
    if (request.method=='GET'):
        return render(request,'posts/signup.html')

    elif (request.method=='POST'):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        username=request.POST['username']
        password= request.POST['password']

        newUser=User.objects.create_user(username=username,password=password,first_name=firstname,last_name=lastname)
        newUser.save()
        return redirect('/')

def signout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return HttpResponse('unautherized request')

def secret(request):
    if request.user.is_authenticated:
        if request.method=='GET':
            return render(request,'posts/secret.html')
        else:
            title=request.POST['title']
            content= request.POST['content']
            password= request.POST['password']
            uid= request.user.id
            user= User.objects.get(id=uid)

            newPost= Post(title=title,content=content,user=user,lock_password=password)
            newPost.is_locked=True
            newPost.save()
            return redirect('/posts')

    else:
        return HttpResponse('user is not logged in')

def requestPassInfo(request,id):
    if request.user.is_authenticated:
        post= Post.objects.get(id=id)

        return render(request,'posts/requestPassInfo.html',{'post':post})
    else:
        return HttpResponse('user is not logged in')

def secretItem(request,id):
    if request.user.is_authenticated:
        fetched_password= request.POST['password']
        post= Post.objects.get(id=id)
        password= post.lock_password

        if password==fetched_password:
            return render(request,'posts/secretItem.html',{'post':post})
        else:
            return HttpResponse('wrong password')
    else:
        return HttpResponse('user is not logged in')


def requestPassMod(request,id): 
    if request.user.is_authenticated:
        post= Post.objects.get(id=id)

        return render(request,'posts/requestPassMod.html',{'post':post})
    else:
        return HttpResponse('user is not logged in')

def ModifySecret(request,id):
    if request.user.is_authenticated:
        fetched_password= request.POST['password']
        post= Post.objects.get(id=id)
        password= post.lock_password

        if password==fetched_password:
            return render(request,'posts/ModifySecret.html',{'post':post})
        else:
            return HttpResponse('wrong password')
    else:
        return HttpResponse('user is not logged in')

def modifySecret(request,id):
    if request.user.is_authenticated:
        title=request.POST['title']
        content=request.POST['content']

        post=Post.objects.get(id=id)
        post.title=title
        post.content=content
        post.save()
        return redirect('/posts')
    else:
        return HttpResponse('user is not logged in')
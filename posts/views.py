from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login

# Create your views here.

def index(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/posts/'+str(user.id))



def posts(request,uid):
    if request.user.is_authenticated:
        posts=Post.objects.filter(user=uid)
        context={
            'posts':posts,
            'uid': uid,
        }
        return render(request,'posts/index.html',context)
    else:
        return HttpResponse("User is not looged in")


def item(request,id,uid):
    if request.user.is_authenticated:
        post= Post.objects.get(id=id,user=uid)
        context={
            'post': post
        }
        print(request.user.id)
        return render(request,'posts/item.html',context)
    else:
        return HttpResponse("User is not logged in")

def modify(request,id,uid):
    if request.user.is_authenticated:
        if (request.method=='GET'):
            post=Post.objects.get(id=id,user=uid)
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
            return redirect('/posts/'+str(uid))
    else:
        return HttpResponse("User is not logged in")


def add(request,uid):
    if request.user.is_authenticated:
        if(request.method =='GET'):
            title=request.GET['title']
            context={
                'title':title,
                'uid':uid
            }
            return render(request,'posts/add.html',context)

        else:
            title=request.POST['title']
            content=request.POST['content']

            user= User.objects.get(id=uid)
            newPost=Post( title=title,content=content,user=user)
            newPost.save()
            return redirect('/posts/'+str(uid))
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
        
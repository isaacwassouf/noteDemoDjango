from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from . import forms

# Create your views here.

def index(request):
    if(request.method=='POST'):
        loginform= forms.logInForm(request.POST)
        if loginform.is_valid():

            username=loginform.cleaned_data['username']
            password=loginform.cleaned_data['password']
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
            modifyform= forms.PostForm(initial={
                'title':post.title,
                'content':post.content
            })

            return render(request,'posts/modify.html',{'form':modifyform,'id':post.id})

        else:
            modifyform= forms.PostForm(request.POST)
            if (modifyform.is_valid()):
                title= modifyform.cleaned_data['title']
                content= modifyform.cleaned_data['content']

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
            addingform= forms.PostForm(initial={'title':title})

            return render(request,'posts/add.html',{'form':addingform})

        else:
            addingform= forms.PostForm(request.POST)
            if (addingform.is_valid()):
                title=addingform.cleaned_data['title']
                content=addingform.cleaned_data['content']

                uid=request.user.id
                user= User.objects.get(id=uid)
                newPost=Post( title=title,content=content,user=user)
                newPost.save()
                return redirect('/posts')
    else:
        return HttpResponse("User is not looged in")

def home(request):
    if(request.method=='GET'):
        login= forms.logInForm()
        return render(request,'posts/login.html',{'form':login})


def signup(request):
    if (request.method=='GET'):
        signupform= forms.SignUpForm()
        return render(request,'posts/signup.html',{'form':signupform})

    elif (request.method=='POST'):
        signupform= forms.SignUpForm(request.POST)
        if (signupform.is_valid()):

            firstname=signupform.cleaned_data['firstname']
            lastname=signupform.cleaned_data['lastname']
            username=signupform.cleaned_data['username']
            password= signupform.cleaned_data['password']

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
            secertadding= forms.Secret()
            return render(request,'posts/secret.html',{'form':secertadding})
        else:
            secretadding= forms.Secret(request.POST)
            if (secretadding.is_valid()):

                title=secretadding.cleaned_data['title']
                content= secretadding.cleaned_data['content']
                password= secretadding.cleaned_data['password']
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

        passwordform= forms.Secret()
        return render(request,'posts/requestPassInfo.html',{'post':post,'form': passwordform})
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

        passwordform= forms.Secret()
        return render(request,'posts/requestPassMod.html',{'post':post,'form': passwordform})
    else:
        return HttpResponse('user is not logged in')

def modifySecret(request,id):
    if request.user.is_authenticated:
        fetched_password= request.POST['password']
        post= Post.objects.get(id=id)
        password= post.lock_password

        if password==fetched_password:
            secretmodify= forms.PostForm(initial={
                'title': post.title,
                'content': post.content
            })
            return render(request,'posts/ModifySecret.html',{'form':secretmodify,'id':post.id})
        else:
            return HttpResponse('wrong password')
    else:
        return HttpResponse('user is not logged in')

def modifiedSecret(request,id):
    if request.user.is_authenticated:
        modifiyform= forms.PostForm(request.POST)
        if (modifiyform.is_valid()):

            title=modifiyform.cleaned_data['title']
            content=modifiyform.cleaned_data['content']

            post=Post.objects.get(id=id)
            post.title=title
            post.content=content
            post.save()
            return redirect('/posts')
    else:
        return HttpResponse('user is not logged in')
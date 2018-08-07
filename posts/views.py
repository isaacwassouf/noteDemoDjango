from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post

# Create your views here.

def index(request):

    posts=Post.objects.all()
    context={
        'posts': posts
    }
    return render(request,'posts/index.html',context)

def item(request,id):
    post= Post.objects.get(id=id)
    context={
        'post': post
    }
    return render(request,'posts/item.html',context)

def modify(request,id):
    post=Post.objects.get(id=id)
    context={
        'post':post
    }
    return render(request,'posts/modify.html',context)

def add(request):
    if(request.method =='GET'):
        title=request.GET['title']
        context={'title':title}
        return render(request,'posts/add.html',context)

    else:
        title=request.POST['title']
        content=request.POST['content']

        newPost=Post( title=title,content=content)
        newPost.save()
        return redirect('/posts')


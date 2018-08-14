from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Post,User

# Create your views here.
# testing vs code with github 
def index(request):
    if(request.method=='POST'):
        username=request.POST['username']
        password=request.POST['password']
        user=User.objects.filter(username=username,password=password)
        if (user.exists()):
            user =User.objects.get(username=username)
            id=user.id
            return redirect('/posts/'+ str(id))



def posts(request,uid):
    posts=Post.objects.filter(user=uid)
    context={
        'posts':posts,
        'uid': uid
    }
    return render(request,'posts/index.html',context)


def item(request,id,uid):
    post= Post.objects.get(id=id,user=uid)
    context={
        'post': post
    }
    return render(request,'posts/item.html',context)

def modify(request,id,uid):
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


def add(request,uid):
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

def home(request):
    if(request.method=='GET'):
        return render(request,'posts/login.html')


def signup(request):
    if (request.method=='GET'):
        return render(request,'posts/signup.html')

    elif (request.method=='POST'):
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        age=request.POST['age']
        username=request.POST['username']
        password= request.POST['password']

        newUser=User(firstname=firstname,lastname=lastname,age=age,username=username,password=password)
        newUser.save()
        return redirect('/posts/'+str(newUser.id))
        
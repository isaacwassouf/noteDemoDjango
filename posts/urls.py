from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('index/',views.index,name='index'),
    path('posts',views.posts,name='posts'),
    path('posts/info/<int:id>', views.item, name='item'),
    path('posts/modify/<int:id>',views.modify,name='modify'),
    path('posts/modify/<int:id>/modified',views.modify,name='modify'),
    path('posts/add',views.add,name='add'),
    path('posts/done',views.add,name='done'),
    path('signup',views.signup,name='signup'),
]
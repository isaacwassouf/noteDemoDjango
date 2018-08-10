from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.home,name="home"),
    path('index/',views.index,name='index'),
    path('posts/<int:uid>',views.posts,name='posts'),
    path('posts/<int:uid>/info/<int:id>', views.item, name='item'),
    path('posts/<int:uid>/modify/<int:id>',views.modify,name='modify'),
    path('posts/<int:uid>/add',views.add,name='add'),
    path('posts/<int:uid>/done',views.add,name='done'),
]
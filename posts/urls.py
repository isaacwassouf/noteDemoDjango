from django.urls import path,include
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('info/<int:id>', views.item, name='item'),
    path('modify/<int:id>',views.modify,name='modify'),
    path('add',views.add,name='add'),
    path('done',views.add,name='done'),
]
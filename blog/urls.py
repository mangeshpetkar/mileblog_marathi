from django.urls import path
from .import views

urlpatterns=[
    path("",views.index,name="index"),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('single_blog',views.single_blog,name='single_blog')

    ]
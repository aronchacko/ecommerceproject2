from unicodedata import name
from django import views
from . import views
from django.urls import path,include

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('contactpage',views.contactpage,name='contactpage'),
    
    path('usercreate',views.usercreate,name="usercreate"),
    path('user_login',views.user_login,name="user_login"),
    path('logout',views.logout,name="logout")
]
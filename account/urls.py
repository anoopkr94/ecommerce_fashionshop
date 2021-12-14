from django.contrib import admin
from django.urls import path
from account import views

urlpatterns = [
    path('register', views.register, name='register'),
    path('reg_seller',views.reg_seller,name='reg_seller'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('forget_pswd', views.forget_pswd, name='forget_pswd'),
    ]
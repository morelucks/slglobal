
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('login_view/', views.login_view, name='login_view' ),

    path('logout/', views.logout, name='logout' ),
    path('register/', views.register, name='register' ),
    ]

from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home' ),
    path('dashboard/', views.dashboard, name='dashboard' ),
    path('login/', views.login, name='login' ),

    path('logout/', views.logout_user, name='logout' ),
    path('register/', views.register, name='register' ),
    ]

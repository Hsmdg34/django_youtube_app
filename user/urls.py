from django.contrib import admin
from django.urls import path
from user import views

app_name="user"

urlpatterns = [
    path('login/',views.LoginUser,name="login"),
    path('logout/',views.LogoutUser,name="logout"),
    path('register/',views.register,name="register"),
    
]

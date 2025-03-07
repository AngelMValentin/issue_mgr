from django.urls import path, include
from django.contrib import admin
from accounts import views 
from django.shortcuts import redirect


urlpatterns = [
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("profile/", lambda request: redirect('home'), name="profile"),
]
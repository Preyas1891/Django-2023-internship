from.import views
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('index/',views.index),
    path('aboutus/',views.aboutus),
    path('homepage/',views.homepage),
    path('contactus/',views.contactus),
    path('login/',views.login),
    path('register/',views.register),
    
]

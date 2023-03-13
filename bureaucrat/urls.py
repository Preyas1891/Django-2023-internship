from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('addbureaucrat/',views.addbureaucrat),
    path('bureaucratform/',views.addbureaucratwithform),
    path('bureaucratupdate/',views.updatebureaucratwithform),
]

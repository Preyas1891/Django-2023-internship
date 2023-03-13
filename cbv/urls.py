from django.contrib import admin
from django.urls import path,include
from .views import FoodCreateView


urlpatterns = [
    path('create/', FoodCreateView.as_view(),name='foodcreate')

]


from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView,DetailView
from.models import food

# Create your views here.

class FoodCreateView(CreateView):
    fields='__all__'
    model = food
    template_name= 'cbv/foodcreate.html'
    success_url ='/cbv/foodlist'

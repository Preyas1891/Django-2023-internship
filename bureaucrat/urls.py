from django.contrib import admin
from django.urls import path,include
from. import views

urlpatterns = [
    path('allbureaucrat/',views.getallbureaucrat, name='getallbureaucrat'),
    path('addbureaucrat/',views.addbureaucrat),
    path('deletebureaucrat/<int:id>',views.deletebureaucrat,name='deletebureaucrat'),
    path('bureaucratform/',views.addbureaucratwithform),
    path('bureaucratupdate/<int:id>',views.updatebureaucratwithform , name='bureaucratupdate'),
    path('bureaucratdetails/<int:id>',views.bureaucratdetails, name='bureaucratdetails'),
]   
 
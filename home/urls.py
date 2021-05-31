from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("",views.homepage,name='Home'),
    path("Contact",views.contacts,name='Contact'),
    path("SubmitContact",views.SubmitContact,name='SubmitContact')

]
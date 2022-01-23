from django.urls import path 
from . import views
#this is a URLConfmodule 
urlpatterns = [
    path('/hello', views.say_hello)
]
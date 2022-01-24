
from django.urls import path 
from . import views

#set up different pages
#linked to functions in view.py
urlpatterns = [
path("", views.index , name="index"),
path("v1/", views.v1, name="view 1"),
] 
# This file is used to map the URL to the view function
from django.urls import path

# Import the views.py file from the same directory

from . import views


urlpatterns = [
    # Syntax of path function: path('URL', view function, name = "name of the URL")
    path('', views.index, name = "index")
]



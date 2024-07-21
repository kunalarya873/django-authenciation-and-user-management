from django.urls import path
from .views import *
urlpatterns = [
    path('get-names/', get_names),
    path("index/", index),
]

from django.urls import path
from .views import *
urlpatterns = [
    path("", send_test_email, name="home"),
    path("smtp/", send_prod_smtp_email, name="smtp"),
]

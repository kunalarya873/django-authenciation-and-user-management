from django.urls import path
from .views import *

urlpatterns = [
    path("product/", ProductView.as_view(), name="product_list"),
    path("demo/", DemoView.as_view(), name="demo"),
]

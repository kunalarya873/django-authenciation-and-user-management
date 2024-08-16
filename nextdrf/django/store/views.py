from django.shortcuts import render
from rest_framework import generics

from . import models
from .models import Category, Product
from .serializers import CategorySerializer, ProductSerializer


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
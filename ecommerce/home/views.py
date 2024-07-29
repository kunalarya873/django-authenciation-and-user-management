from django.shortcuts import render
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from rest_framework.permissions import AllowAny, IsAuthenticated

class ProductView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        queryset = Product.objects.all()
        serializers = ProductSerializer(queryset, many=True)
        return Response(serializers.data)
    
class DemoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        return Response({"success": "You are authenticated"})
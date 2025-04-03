

from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import User, Product
from .serializers import ProductSerializer, UserSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response


class ProductList(generics.ListCreateAPIView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer



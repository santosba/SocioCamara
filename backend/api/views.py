

from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import User, Product , OrderItem, Order
from .serializers import ProductSerializer, UserSerializer,OrderItemSerializer, OrderSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.filters import ProductFilter


class ProductList(generics.ListCreateAPIView):
    template_name = 'product_list.html'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter
    
    
    
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filterset_class = ProductFilter

    
    def get_queryset(self):
        queryset = super().get_queryset()
        product_id = self.kwargs.get('id')
        return queryset.filter(id=product_id)
        

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer



class order_list(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer






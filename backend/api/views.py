

from rest_framework import generics
from django.shortcuts import get_object_or_404
from .models import User, Product , OrderItem, Order
from book.models import Book,BookReview
from .serializers import BookReviewSerializer, ProductSerializer, UserSerializer,OrderItemSerializer, OrderSerializer,BookSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_filters.rest_framework import DjangoFilterBackend
from api.filters import ProductFilter


class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [ 'price']

    '''
     def get(self, request):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
    ''' 
                   
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"

    def get(self, request, *args, **kwargs):

        try:
            product = self.get_queryset().get(id=kwargs.get('id'))
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(product)
        return Response(serializer.data) 
    
    def put(self, request, *args, **kwargs):
        product = self.get_queryset().get(id=kwargs.get('id'))
        serializer = self.serializer_class(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request ,*args, **kwargs):
        product = self.get_queryset().get(id=kwargs.get('id'))
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
     

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer





class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field ='id'

    def get_object(self):
       id_ = self.kwargs.get('id')
       return get_object_or_404(User,pk=id_)
    
    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.serializer_class(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class order_list(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'id'

class BookReviewList(generics.ListAPIView):
    
    serializer_class = BookReviewSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')

        return BookReview.objects.filter(book=book_id)
    
class BookReviewCreate(generics.CreateAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    
    def perform_create(self, serializer):

        id_book = self.kwargs.get('book_id')
        book = Book.objects.get(id=id_book)
        serializer.save(book=book, author=self.request.user)
       

class BookReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer
    lookup_field = 'id'



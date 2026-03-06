# backend/api/serializers.py
from rest_framework import serializers
from .models import Product, OrderItem, Order,User

from book.models import Book, BookReview

class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True,style={'input_type':'password'})
    class Meta:
        model = User
        fields = ['username','email','password','password2']
        extra_kwargs = {
            'password' : {'write_only':True}
        }

    def save(self):
        password = self._validated_data['password']
        password2 = self._validated_data['password2']

        if password !=password2:
            raise serializers.ValidationError({'error':'password and password2 must be the same'})
        
        if User.objects.filter(email=self._validated_data['email']).exists():
            raise serializers.ValidationError({'error':'Email already exists'})
        
        user = User(
            username = self._validated_data['username'],
            email = self._validated_data['email'],
            password = self._validated_data['password']
        )
        user.set_password(self._validated_data['password'])
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields ='__all__'

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError('Price must be greater than 0')
        return value
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class OrderItemSerializer(serializers.ModelSerializer):
   # product_details = ProductSerializer(source='product', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = [ 'quantity', 'price', ]
        read_only_fields = ['item_subtotal']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    total_price = serializers.SerializerMethodField(method_name='total')


    def total(self, obj):
        return sum(item.item_subtotal for item in obj.items.all())
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'status', 'items',  'total_price']
        read_only_fields = ['total']





class BookReviewSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    class Meta:
        model = BookReview
        fields = ['book', 'review', 'rating', 'author', 'created_at']
        read_only_fields = ['id','book']

class BookSerializer(serializers.ModelSerializer):
    reviews = BookReviewSerializer(many=True , read_only=True)
    class Meta:
        model = Book
        fields = ['title','author','price','cover','published','reviews']
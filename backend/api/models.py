from itertools import product
import uuid
from django.db import models

from django.contrib.auth.models import AbstractUser
from enum import Enum


class User(AbstractUser):
    email = models.EmailField(unique=True)
  

    USERNAME_FIELD = 'username'
   # REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
    

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    @property
    def in_stock(self):
        return self.stock > 0

    def __str__(self):
        return self.name
    
class Order(models.Model): 
    class StatusChoices(models.TextChoices):
        PENDING = 'Pending'
        PROCESSING = 'Processing'
        SHIPPED = 'Shipped'
        DELIVERED = 'Delivered'
        CANCELLED = 'Cancelled'

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, through='OrderItem', related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)          
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=10, choices=StatusChoices.choices, default=StatusChoices.PENDING)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def item_subtotal(self):
        return self.product.price * self.quantity
    
    def __str__(self):
        return f"Order {self.order.id} - Product {self.product.name} - Qty {self.quantity}"
    

# Create your models here.


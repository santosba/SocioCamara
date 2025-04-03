# backend/api/management/commands/populate_db.py
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from django.core.management.base import BaseCommand
from faker import Faker
from api.models import User, Product, Order, OrderItem

from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Populate database with fake data'
    def handle(self, *args, **kwargs):
        # get or create superuser

        user = User.objects.filter(username='admin').first()
        if not user:
            user = User.objects.create_superuser(username='admin',password='password123')
        fake = Faker()
        
        # Create Users (10)
        users = []
        for _ in range(10):
            user = User.objects.create(
                username=fake.user_name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name()
            )
            user.set_password('password123')
            user.save()
            users.append(user)
            
        # Create Products (20)
        products = []
        for _ in range(20):
            product = Product.objects.create(
                name=fake.catch_phrase(),
                description=fake.text(),
                price=Decimal(random.uniform(10.0, 1000.0)).quantize(Decimal('0.01'))
            )
            products.append(product)
            
        # Create Orders (30)
        for _ in range(30):
            user = random.choice(users)
            order = Order.objects.create(
                user=user,
                total=Decimal('0'),
                status=random.choice(Order.StatusChoices.choices)[0]
            )
            
            # Create OrderItems (1-5 per order)
            order_total = Decimal('0')
            for _ in range(random.randint(1, 5)):
                product = random.choice(products)
                quantity = random.randint(1, 5)
                price = product.price
                
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    price=price
                )
                order_total += price * quantity
            
            order.total = order_total
            order.save()

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))
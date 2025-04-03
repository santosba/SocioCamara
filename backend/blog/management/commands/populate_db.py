# backend/api/management/commands/populate_db.py
import sys
import os

# Adiciona o diretório raiz do projeto ao sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import FeaturedArticle, NormalArticle

from decimal import Decimal
import random


class Command(BaseCommand):
    help = 'Populate database with fake data'

    def handle(self, *args, **kwargs):
        # get or create superuser

       feactured_article = FeaturedArticle.objects.filter(title='featured').first()
       
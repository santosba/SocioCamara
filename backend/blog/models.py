from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from PIL import Image

def validate_image_dimensions(image, max_width, max_height):
    img = Image.open(image)
    if img.width > max_width or img.height > max_height:
        raise ValidationError(f"Image dimensions should not exceed {max_width}x{max_height} pixels")



def validate_featured_image(image):
    validate_image_dimensions(image, 800, 350)

def validate_normal_image(image):
    validate_image_dimensions(image, 350, 350)


def validate_image(image):
    img = Image.open(image)
    max_width, max_height = 1024, 800
    min_width, min_height = 500, 400
    if not (min_width <= img.width <= max_width and min_height <= img.height <= max_height):
        raise ValidationError(f"Image dimensions must be between {min_width}x{min_height} and {max_width}x{max_height} pixels")




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

class Article(models.Model):
    ARTICLE_TYPE_CHOICES = [
        ('normal', 'Normal'),
        ('featured', 'Featured'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/', validators=[validate_image])
    article_type = models.CharField(max_length=10, choices=ARTICLE_TYPE_CHOICES, default='normal')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

        


    

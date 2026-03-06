from django.conf import settings
from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
from PIL import Image
from django.urls import reverse

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
    min_width = 500
    if img.width < min_width:
        raise ValidationError(f"Image width must be at least {min_width} pixels")




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
    slug = models.SlugField(max_length=250,unique_for_date='created_at')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='covers/', validators=[validate_image])
    article_type = models.CharField(max_length=10, 
                                    choices=ARTICLE_TYPE_CHOICES, default='normal')
    category = models.ForeignKey('Category', 
                                 on_delete=models.CASCADE,
                                  related_name='articles',default=1)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('blog:article-detail', args=[
            self.created_at.year,
            self.created_at.month,
            self.created_at.day,
            self.slug
            ])

    class Meta:
        verbose_name = 'Article'
        verbose_name_plural = 'Articles'

        


    

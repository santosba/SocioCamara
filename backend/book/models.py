from PIL import Image
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse

# Create your models here.

class Book(models.Model):


    def validate_image(image):
        try:
            img = Image.open(image)
            img.verify()
        except:
            raise ValidationError('Image is not valid')
        
    
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    cover = models.ImageField(upload_to='covers/', 
                              blank=True,
                              validators=[validate_image],
                              help_text='Maximum size of 10MB')
    published = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    

    def get_absolute_url(self):
        return reverse('book:book-list')
    

 
from django.db import models
from django.db.models import CASCADE
from django.forms import ValidationError
from django.utils import timezone
from django.conf import settings
from PIL import Image

# Create your models here.

def validate_image(image):
    img = Image.open(image)
    min_width = 500
    if img.width < min_width:
        raise ValidationError(f"Image width must be at least {min_width} pixels")

class Actividade(models.Model):
    nome = models.TextField(max_length=245)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.nome    

class FormaJuridica(models.Model):
    nome = models.TextField(max_length=245)
    description = models.TextField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.nome

class Socio(models.Model):
    nome = models.TextField(max_length=245)
    SOCIO_TYPE_CHOICES = [
        ('empresa', 'Empresa'),
        ('individual', 'Individual'),
    ]
    tipo_socio = models.CharField(max_length=10, choices=SOCIO_TYPE_CHOICES)
    telefone = models.CharField(max_length=15, default='', blank=True)
    email = models.EmailField(default='', blank=True)
    morada = models.TextField(max_length=500, default='', blank=True)
    data_registo = models.DateTimeField(default=timezone.now)
    actividade = models.ForeignKey('Actividade', on_delete=CASCADE,
                                   related_name='socios', default=1, blank=True, null=True
            )
    forma = models.ForeignKey('FormaJuridica', on_delete=CASCADE, related_name='socios',
                              default=1, blank=True, null=True)
    


    def __str__(self):
        return f"Comentário de {self.autor} em {self.artigo}"

class Artigo(models.Model):
    class Article_type(models.TextChoices):
        FEATURED = 'FE', 'Feactured'
        NORMAL = 'NR', 'Normal'
    titulo = models.TextField(max_length=245)
    conteudo = models.TextField(max_length=5000)
    data_publicacao = models.DateTimeField(default=timezone.now)
    views = models.PositiveIntegerField(default=0)
    image =models.ImageField(upload_to='artigos/',validators=[validate_image],blank=True)
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='artigos')
    categoria = models.ForeignKey('Categoria', on_delete=CASCADE,
                                   related_name='artigos', default=1)
    tipo_artigo = models.CharField(max_length=20, choices=Article_type.choices, default=Article_type.NORMAL)
    def __str__(self):
        return self.titulo
    
    def increment_views(self):
        self.views += 1
        self.save(update_fields=['views'])


    def MostViews_article(self):

        return Artigo.objects.all().order_by('-views')[:5]

        


    
    class Meta:
        ordering = ['-data_publicacao']
        indexes = [
            models.Index(fields=['-data_publicacao'])
        ]


class Comentario(models.Model):
    artigo = models.ForeignKey('Artigo', on_delete=CASCADE, related_name='comentarios')
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=CASCADE, related_name='comentarios')
    conteudo = models.TextField(max_length=1000)
    data_publicacao = models.DateTimeField(default=timezone.now)
    
class Categoria(models.Model):
    nome = models.TextField(max_length=245)
    descricao = models.TextField(max_length=500, default='', blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

class TradingInfo(models.Model):
    titulo = models.CharField(max_length=200)
    image = models.ImageField(upload_to='artigos/',validators=[validate_image],blank=True)

class Contacto(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} - {self.data_envio.strftime('%Y-%m-%d %H:%M:%S')}"
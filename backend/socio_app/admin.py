from django.contrib import admin

from .models import Categoria, Socio, Actividade, FormaJuridica,Artigo, TradingInfo
from .forms import SocioForm ,ArtigoForm,CategoriaForm        

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm
    list_display = ('nome', 'telefone', 'email', 'morada', 'data_registo', 'actividade', 'forma', 'tipo_socio')
    search_fields = ('nome', 'email')
    list_filter = ('data_registo', 'email')
    fieldsets = (
        ('Informação Pessoal', {
            'fields': ('nome', 'telefone', 'email', 'morada', 'tipo_socio'),
            'classes': ('wide',)
        }),
        ('Informação de Registo', {
            'fields': ('data_registo',),    
            'classes': ('wide',)
        }),
        ('Atividade', {
            'fields': ('actividade',),  # Mostra o campo ForeignKey, mas no list_display mostra o nome
            'classes': ('wide',)
        }),
        ('Forma Jurídica', {
            'fields': ('forma',),  # Mostra o campo ForeignKey, mas no list_display mostra o nome
            'classes': ('wide',)
        })
    )

   


@admin.register(Actividade)
class ActividadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'description')
    search_fields = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'description')
        }),
    )   
@admin.register(FormaJuridica)
class FormaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'description')
    search_fields = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'description')
        }),
    )    

@admin.register(TradingInfo)
class TradingInfoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'image')
    search_fields = ('titulo',)
    fieldsets = (
        (None, {
            'fields': ('titulo', 'image')
        }),
    )     

@admin.register(Artigo)
class ArtigoAdmin(admin.ModelAdmin):
    form = ArtigoForm
    list_display = ('titulo', 'data_publicacao', 'conteudo', 'image',
                     'autor', 'categoria','tipo_artigo')
    search_fields = ('titulo', 'conteudo')
    list_filter = ('data_publicacao','categoria')
    fieldsets = (
        ('Informação do Artigo', {
            'fields': ('titulo', 'conteudo',  'image', 'categoria', 'tipo_artigo')
        }),
        ('Publicação', {
            'fields': ('data_publicacao',),
            'classes': ('wide',)
        }),
        ('Autor', {
            'fields': ('autor',),
            'classes': ('wide',)
        })
    )

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    form = CategoriaForm
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'descricao')
        }),
    )
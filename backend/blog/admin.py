from django.contrib import admin
from .models import Article, Category
from .forms import UnifiedArticleForm



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = UnifiedArticleForm
    list_display = ('title','slug' ,'author', 'created_at', 'is_published', 'article_type','category')
    list_filter = ('is_published', 'created_at', 'author', 'article_type')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Article Information', {
            'fields': ('title','slug' ,'content', 'author', 'is_published', 'article_type')
        }),
        ('Media', {
            'fields': ('image',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),(
            'Category', {
                'fields': ('category',)
            }                                       
        )
    )
              

    @admin.register(Category)
    class CategoryAdmin(admin.ModelAdmin):
        list_display = ('name', 'description')
        search_fields = ('name',)
        fieldsets = (
            (None, {
                'fields': ('name', 'description')
            }),
        )
    
from django.contrib import admin
from .models import Article
from .forms import UnifiedArticleForm



@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = UnifiedArticleForm
    list_display = ('title', 'author', 'created_at', 'is_published', 'article_type')
    list_filter = ('is_published', 'created_at', 'author', 'article_type')
    search_fields = ('title', 'content')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Article Information', {
            'fields': ('title', 'content', 'author', 'is_published', 'article_type')
        }),
        ('Media', {
            'fields': ('image',),
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
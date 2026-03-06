from django.contrib import admin

from .models import  Book,BookReview

# Register your models h
class BookReviewInline(admin.TabularInline):
    model = BookReview
    extra = 1

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    inlines = [BookReviewInline]

# cms/models.py - Simple CMS models
from django.db import models
from django.conf import settings
import json

class Page(models.Model):
    """A webpage that can be built with components"""
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL path for this page")
    
    # Store the page structure as JSON
    # Example: {"components": [{"type": "text", "content": "Hello"}]}
    content = models.JSONField(default=dict, help_text="Page structure and components")
    
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-updated_at']


class ComponentType(models.Model):
    """Define what types of components are available"""
    name = models.CharField(max_length=100, help_text="Display name (e.g., 'Text Block')")
    type_key = models.CharField(max_length=50, unique=True, help_text="Internal key (e.g., 'text')")
    
    # Define what properties this component has
    # Example: {"content": {"type": "string", "default": ""}, "font_size": {"type": "number", "default": 16}}
    schema = models.JSONField(help_text="Component properties definition")
    
    # Template file to render this component
    template_name = models.CharField(max_length=200, help_text="Template file path")
    
    is_active = models.BooleanField(default=True)
    icon = models.CharField(max_length=50, blank=True, help_text="CSS icon class")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class SavedComponent(models.Model):
    """Save reusable component configurations"""
    name = models.CharField(max_length=100)
    component_type = models.ForeignKey(ComponentType, on_delete=models.CASCADE)
    config = models.JSONField(help_text="Saved component configuration")
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.component_type.name})"
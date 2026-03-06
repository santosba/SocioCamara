# cms/serializers.py - API data serialization
from rest_framework import serializers
from .models import Page, ComponentType, SavedComponent
from .services import ComponentValidator

class ComponentTypeSerializer(serializers.ModelSerializer):
    """Serialize component types for the frontend"""
    
    class Meta:
        model = ComponentType
        fields = ['id', 'name', 'type_key', 'schema', 'icon']

class PageSerializer(serializers.ModelSerializer):
    """Serialize pages for the API"""
    
    class Meta:
        model = Page
        fields = ['id', 'title', 'slug', 'content', 'is_published', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
    
    def validate_content(self, value):
        """Validate page content structure"""
        if not isinstance(value, dict):
            raise serializers.ValidationError("Content must be a JSON object")
        
        components = value.get('components', [])
        if not isinstance(components, list):
            raise serializers.ValidationError("Components must be a list")
        
        # Validate each component
        for i, component in enumerate(components):
            is_valid, errors = ComponentValidator.validate_component(component)
            if not is_valid:
                raise serializers.ValidationError(f"Component {i}: {', '.join(errors)}")
        
        return value

class SavedComponentSerializer(serializers.ModelSerializer):
    """Serialize saved components"""
    component_type_name = serializers.CharField(source='component_type.name', read_only=True)
    
    class Meta:
        model = SavedComponent
        fields = ['id', 'name', 'component_type', 'component_type_name', 'config']
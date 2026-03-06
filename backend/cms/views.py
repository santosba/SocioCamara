# cms/views.py - API endpoints
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Page, ComponentType, SavedComponent
from .serializers import PageSerializer, ComponentTypeSerializer, SavedComponentSerializer
from .services import ComponentRenderer

class ComponentTypeListView(generics.ListAPIView):
    """
    Get list of available component types for the drag-and-drop palette
    
    Example response:
    [
        {
            "id": 1,
            "name": "Text Block",
            "type_key": "text",
            "schema": {"content": {"type": "string", "default": ""}},
            "icon": "fa fa-text"
        }
    ]
    """
    queryset = ComponentType.objects.filter(is_active=True)
    serializer_class = ComponentTypeSerializer

class PageListCreateView(generics.ListCreateAPIView):
    """
    List all pages or create a new page
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    
    def perform_create(self, serializer):
        # Set the current user as author
        serializer.save(author=self.request.user)

class PageDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Get, update, or delete a specific page
    """
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    lookup_field = 'slug'  # Use slug instead of ID in URLs

@api_view(['GET'])
def preview_page(request, slug):
    """
    Preview a page (render the actual HTML)
    
    This endpoint returns the rendered HTML of the page
    """
    page = get_object_or_404(Page, slug=slug)
    
    # Render the page content
    html_content = ComponentRenderer.render_page(page, request)
    
    # Wrap in a basic HTML structure
    full_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>{page.title}</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            body {{ 
                font-family: Arial, sans-serif; 
                margin: 0; 
                padding: 20px; 
                line-height: 1.6; 
            }}
            .error {{ 
                color: red; 
                border: 1px solid red; 
                padding: 10px; 
                margin: 10px 0; 
            }}
        </style>
    </head>
    <body>
        <h1>{page.title}</h1>
        {html_content}
    </body>
    </html>
    """
    
    return HttpResponse(full_html, content_type='text/html')

@api_view(['POST'])
def validate_component(request):
    """
    Validate a component configuration
    
    POST data: {"type": "text", "config": {"content": "Hello"}}
    Response: {"is_valid": true, "errors": []}
    """
    from .services import ComponentValidator
    
    component_data = request.data
    is_valid, errors = ComponentValidator.validate_component(component_data)
    
    return Response({
        'is_valid': is_valid,
        'errors': errors
    })

class SavedComponentListCreateView(generics.ListCreateAPIView):
    """
    List saved components or save a new component configuration
    """
    serializer_class = SavedComponentSerializer
    
    def get_queryset(self):
        return SavedComponent.objects.filter(created_by=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
# cms/services.py - Component rendering logic
from django.template.loader import get_template
from django.template import Context, RequestContext
from .models import ComponentType

class ComponentRenderer:
    """
    This class handles rendering components into HTML
    Think of it as a translator: JSON config → HTML output
    """
    
    @staticmethod
    def render_component(component_data, request=None):
        """
        Render a single component
        
        Args:
            component_data: {"type": "text", "config": {"content": "Hello"}}
            request: Django request object (optional)
        
        Returns:
            Rendered HTML string
        """
        try:
            # Get component type info
            component_type = ComponentType.objects.get(
                type_key=component_data.get('type'),
                is_active=True
            )
            
            # Load the template
            template = get_template(component_type.template_name)
            
            # Prepare context (data to pass to template)
            context = {
                'config': component_data.get('config', {}),
                'component_type': component_type,
                'request': request
            }
            
            # Render and return HTML
            if request:
                context = RequestContext(request, context)
            
            return template.render(context)
            
        except ComponentType.DoesNotExist:
            # Component type not found - show error
            return f'<div class="error">Unknown component type: {component_data.get("type")}</div>'
        except Exception as e:
            # Any other error - show error message
            return f'<div class="error">Error rendering component: {str(e)}</div>'
    
    @staticmethod
    def render_page(page, request=None):
        """
        Render a complete page
        
        Args:
            page: Page model instance
            request: Django request object (optional)
        
        Returns:
            Complete HTML for the page
        """
        html_parts = []
        
        # Get components from page content
        components = page.content.get('components', [])
        
        # Render each component
        for component_data in components:
            html = ComponentRenderer.render_component(component_data, request)
            html_parts.append(html)
        
        # Join all HTML parts
        return '\n'.join(html_parts)


class ComponentValidator:
    """
    Validates component data against schemas
    """
    
    @staticmethod
    def validate_component(component_data):
        """
        Check if component data is valid
        
        Args:
            component_data: {"type": "text", "config": {...}}
        
        Returns:
            (is_valid: bool, errors: list)
        """
        errors = []
        
        try:
            # Check if component type exists
            component_type = ComponentType.objects.get(
                type_key=component_data.get('type'),
                is_active=True
            )
            
            # Get component schema (rules)
            schema = component_type.schema
            config = component_data.get('config', {})
            
            # Validate each field
            for field_name, field_rules in schema.items():
                if field_rules.get('required') and field_name not in config:
                    errors.append(f"Field '{field_name}' is required")
                
                # Check data types
                if field_name in config:
                    expected_type = field_rules.get('type')
                    value = config[field_name]
                    
                    if expected_type == 'string' and not isinstance(value, str):
                        errors.append(f"Field '{field_name}' must be a string")
                    elif expected_type == 'number' and not isinstance(value, (int, float)):
                        errors.append(f"Field '{field_name}' must be a number")
            
            return len(errors) == 0, errors
            
        except ComponentType.DoesNotExist:
            return False, [f"Component type '{component_data.get('type')}' does not exist"]
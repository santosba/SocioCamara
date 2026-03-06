# cms/management/commands/setup_cms_components.py
from django.core.management.base import BaseCommand
from cms.models import ComponentType

class Command(BaseCommand):
    help = 'Set up default CMS component types'

    def handle(self, *args, **options):
        """Create the basic component types"""
        
        components = [
            {
                'name': 'Text Block',
                'type_key': 'text',
                'template_name': 'components/text.html',
                'icon': 'fa fa-font',
                'schema': {
                    'content': {
                        'type': 'string',
                        'default': 'Enter your text here...',
                        'label': 'Content',
                        'required': True
                    },
                    'font_size': {
                        'type': 'number',
                        'default': 16,
                        'label': 'Font Size (px)',
                        'min': 8,
                        'max': 72
                    },
                    'color': {
                        'type': 'color',
                        'default': '#000000',
                        'label': 'Text Color'
                    },
                    'align': {
                        'type': 'select',
                        'default': 'left',
                        'label': 'Text Alignment',
                        'options': ['left', 'center', 'right', 'justify']
                    },
                    'margin': {
                        'type': 'number',
                        'default': 10,
                        'label': 'Margin (px)',
                        'min': 0,
                        'max': 100
                    }
                }
            },
            {
                'name': 'Image',
                'type_key': 'image',
                'template_name': 'components/image.html',
                'icon': 'fa fa-image',
                'schema': {
                    'src': {
                        'type': 'string',
                        'default': '/static/placeholder.jpg',
                        'label': 'Image URL',
                        'required': True
                    },
                    'alt': {
                        'type': 'string',
                        'default': 'Image',
                        'label': 'Alt Text'
                    },
                    'width': {
                        'type': 'number',
                        'default': 100,
                        'label': 'Width (%)',
                        'min': 1,
                        'max': 100
                    },
                    'max_width': {
                        'type': 'number',
                        'default': 600,
                        'label': 'Max Width (px)',
                        'min': 100,
                        'max': 2000
                    },
                    'border_radius': {
                        'type': 'number',
                        'default': 0,
                        'label': 'Border Radius (px)',
                        'min': 0,
                        'max': 50
                    },
                    'align': {
                        'type': 'select',
                        'default': 'left',
                        'label': 'Alignment',
                        'options': ['left', 'center', 'right']
                    },
                    'caption': {
                        'type': 'string',
                        'default': '',
                        'label': 'Caption (optional)'
                    }
                }
            },
            {
                'name': 'Button',
                'type_key': 'button',
                'template_name': 'components/button.html',
                'icon': 'fa fa-square',
                'schema': {
                    'text': {
                        'type': 'string',
                        'default': 'Click Me',
                        'label': 'Button Text',
                        'required': True
                    },
                    'url': {
                        'type': 'string',
                        'default': '#',
                        'label': 'Link URL',
                        'required': True
                    },
                    'bg_color': {
                        'type': 'color',
                        'default': '#007bff',
                        'label': 'Background Color'
                    },
                    'text_color': {
                        'type': 'color',
                        'default': '#ffffff',
                        'label': 'Text Color'
                    },
                    'font_size': {
                        'type': 'number',
                        'default': 16,
                        'label': 'Font Size (px)',
                        'min': 8,
                        'max': 32
                    },
                    'padding': {
                        'type': 'number',
                        'default': 10,
                        'label': 'Padding (px)',
                        'min': 5,
                        'max': 30
                    },
                    'border_radius': {
                        'type': 'number',
                        'default': 4,
                        'label': 'Border Radius (px)',
                        'min': 0,
                        'max': 20
                    },
                    'align': {
                        'type': 'select',
                        'default': 'left',
                        'label': 'Alignment',
                        'options': ['left', 'center', 'right']
                    },
                    'target': {
                        'type': 'select',
                        'default': '',
                        'label': 'Link Target',
                        'options': ['', '_blank', '_self']
                    }
                }
            }
        ]
        
        created_count = 0
        updated_count = 0
        
        for comp_data in components:
            component, created = ComponentType.objects.get_or_create(
                type_key=comp_data['type_key'],
                defaults=comp_data
            )
            
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created component type: {component.name}')
                )
            else:
                # Update existing component
                for key, value in comp_data.items():
                    setattr(component, key, value)
                component.save()
                updated_count += 1
                self.stdout.write(
                    self.style.WARNING(f'Updated component type: {component.name}')
                )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Setup complete! Created {created_count} new, updated {updated_count} existing component types.'
            )
        )
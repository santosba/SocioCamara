# cms/urls.py
from django.urls import path
from . import views

app_name = 'cms'

urlpatterns = [
    # Component types for the palette
    path('component-types/', views.ComponentTypeListView.as_view(), name='component-types'),
    
    # Pages CRUD
    path('pages/', views.PageListCreateView.as_view(), name='page-list'),
    path('pages/<slug:slug>/', views.PageDetailView.as_view(), name='page-detail'),
    
    # Page preview
    path('preview/<slug:slug>/', views.preview_page, name='page-preview'),
    
    # Component validation
    path('validate-component/', views.validate_component, name='validate-component'),
    
    # Saved components
    path('saved-components/', views.SavedComponentListCreateView.as_view(), name='saved-components'),
]
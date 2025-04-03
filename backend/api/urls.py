from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductList,UserList
"""
router = SimpleRouter()
router.register('', views.ProductViewSet, basename='product')
router.register(r'use




rs', views.UserViewSet, basename='user')
"""

urlpatterns = [
   path('', ProductList.as_view(), name='product-list'),
   #path('products/<int:id>/', views.product_detail, name='product-detail'),
   path('users/', UserList.as_view(), name='user-list'),
    # Add your additional URL patterns here
    # Example: path('specific-endpoint/', views.SpecificView.as_view(), name='specific-view'),
]




#urlpatterns = router.urls

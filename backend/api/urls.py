from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import ProductList,UserList, ProductDetail


urlpatterns = [
   path('', ProductList.as_view(), name='product-list'),
   path('product/<int:id>/', ProductDetail.as_view(), name='product-detail'),
   path('users/', UserList.as_view(), name='user-list'),
    # Add your additional URL patterns here
    # Example: path('specific-endpoint/', views.SpecificView.as_view(), name='specific-view'),
]




#urlpatterns = router.urls

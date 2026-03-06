from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import (ProductList,UserList, 
                    ProductDetail,
                    order_list,BookList,UserDetail,
                    BookDetail,BookReviewList,BookReviewDetail,BookReviewCreate)


urlpatterns = [
   path('', ProductList.as_view(), name='product-list'),
   path('product/<int:id>/', ProductDetail.as_view(), name='product-detail'),
   path('orders/', order_list.as_view(), name='order-list'),
   path('book/', BookList.as_view(), name='book-list'),
   path('book/<int:id>/', BookDetail.as_view(), name='book-detail'),
   path('book/<int:book_id>/reviews/create', BookReviewCreate.as_view(), name='bookreview-create'),
   path('book/<int:book_id>/reviews/', BookReviewList.as_view(), name='bookreview-list'),
   path('reviews/<int:review_id>/', BookReviewDetail.as_view(), name='bookreview-detail'),
   path('users/', UserList.as_view(), name='user-list'),
   path('users/<int:id>', UserDetail.as_view(), name='user-detail'),
]

#urlpatterns = router.urls
                                                                                                                                                                                                                                                                                                                                                                                                                                           
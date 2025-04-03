from django.urls import path
from .views import ArticleListView, SignupPageView

urlpatterns = [
    path('', ArticleListView.as_view(), name='blog_index'),
    path('', SignupPageView.as_view(), name='signup'),
]

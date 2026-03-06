from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import BookListView, BookDetailView,createBookview
app_name = 'book'
urlpatterns = [
    path('', BookListView.as_view(), name='book-list'),
    path('<int:id>/', BookDetailView.as_view(), name='book-detail'),
    path('create/', createBookview.as_view(), name='new'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

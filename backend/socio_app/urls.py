
from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from .views import HomeView,PostDetailView, ArticlesByCategoryView

app_name = 'camera'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('post/<int:id_post>/', PostDetailView.as_view(), name='post_detail'),
    path('api/articles-by-category/', ArticlesByCategoryView.as_view(), name='articles_by_category'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
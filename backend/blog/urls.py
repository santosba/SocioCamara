from django.urls import path
from .views import ArticleListView, SignupPageView,ArticleDetailView,CategoryDetailView, SearchResultsView
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'
urlpatterns = [
    path('', ArticleListView.as_view(), name='article-list'),
    path('<int:year>/<int:month>/<int:day>/<slug:slug>/', ArticleDetailView.as_view(), name='article-detail'),
    path('category/<int:id_cat>/', CategoryDetailView.as_view(), name='category_detail'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('', SignupPageView.as_view(), name='signup'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
  
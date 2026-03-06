from django.views.generic import ListView, DetailView, CreateView

from django.db.models import Q
from django.shortcuts import get_object_or_404
from .models import Article,Category

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    queryset = Article.objects.filter(article_type='normal').order_by('-created_at')
    paginate_by = 6  # Show 6 normal articles per page (2 rows of 3)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['featured_article'] = Article.objects.filter(article_type='featured').order_by('-created_at').first()
        # Use paginated queryset for normal articles
        context['normal_articles'] = context['articles']
        return context

class ArticleDetailView(DetailView):
    model = Article
    queryset = Article.objects.all()
    template_name = 'blog/article_detail.html'

    def get_object(self):
        #id_ = self.kwargs.get('id')
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        slug = self.kwargs.get('slug')
        return get_object_or_404(Article
                                   , created_at__year=year
                                   , created_at__month=month
                                   , created_at__day=day
                                   , slug=slug)
    


class CategoryDetailView(ListView):
    model = Article
    template_name = 'blog/category_detail.html'
    context_object_name = 'categories_articles'

    def get_queryset(self):
        category_id = self.kwargs.get('id_cat')
        return Article.objects.filter(category_id=category_id)


class SearchResultsView(ListView):
    model = Article
    template_name = 'blog/search_results.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Article.objects.filter( Q(title__icontains=query) | Q(content__icontains=query) )

   


class SignupPageView(CreateView):
    template_name = 'registration/signup.html'




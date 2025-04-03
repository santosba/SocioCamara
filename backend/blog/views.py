from django.views.generic import ListView, DetailView, CreateView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/home.html'
    context_object_name = 'articles'
    queryset = Article.objects.filter(is_published=True)


    paginate_by = 10

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'
    context_object_name = 'article'



class SignupPageView(CreateView):
    template_name = 'registration/signup.html'

    
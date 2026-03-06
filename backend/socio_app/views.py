from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from .models import  Artigo, TradingInfo, Categoria

from .forms import ContactoForm,CommentForm


class HomeView(ListView):
    template_name = 'socio/home.html'
    model = Artigo 
    queryset = Artigo.objects.all()

    form_class = ContactoForm

    
    def get(self, request, **kwargs):
        self.object_list = self.get_queryset()
        context = self.get_context_data(**kwargs)
        form = self.form_class()
        return render(request, self.template_name, {'ContactForm': form, **context})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'socio/contact_success.html')
        else:
            return render(request, self.template_name, {'ContactForm': form})
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['most_viewed_articles'] = Artigo.MostViews_article(self)
        context['trading_news'] = TradingInfo.objects.all().order_by('-id').first()
        context['artigo_destaque'] = Artigo.objects.filter(tipo_artigo='FE').order_by('-id').first()
        context['artigo_normal'] = Artigo.objects.filter(tipo_artigo='NR').order_by('-id')[1:6]
        context['artigo_servico'] = Artigo.objects.filter(categoria__nome='servicos').order_by('-id')[:3]
        context['artigo_noticias'] = Artigo.objects.filter(categoria__nome='noticias').order_by('-id')[:5]
        context['categories'] = Categoria.objects.all()
        return context
    
class PostDetailView(DetailView):
        
    template_name = 'socio/post_detail.html'
    model = Artigo
    context_object_name = 'artigo'

    def get_object(self):
        id_ = self.kwargs.get('id_post')

        artigo = get_object_or_404( Artigo,id = id_)
        # Increment view count
        artigo.increment_views()
        return  artigo


class CreateCommentView(ListView):
    template_name = 'socio/post_detail.html'

    form_class = CommentForm


    def get(self, request, *args, **kwargs):

        form = self.form_class

        return render(request,self.template_name,{'CommentForm',form})

'''

def get_articles_by_category(request):
    """AJAX view to get articles filtered by category"""
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        category_name = request.GET.get('category', '').lower()
        
        if category_name:
            articles = Artigo.objects.filter(categoria__nome__iexact=category_name).order_by('-data_publicacao')[:6]
        else:
            articles = Artigo.objects.all().order_by('-data_publicacao')[:6]
        
        # Prepare article data for JSON response
        articles_data = []
        for article in articles:
            articles_data.append({
                'id': article.id,
                'titulo': article.titulo,
                'conteudo': article.conteudo[:200] + '...' if len(article.conteudo) > 200 else article.conteudo,
                'data_publicacao': article.data_publicacao.strftime('%b %d, %Y'),
                'views': article.views,
                'image_url': article.image.url if article.image else '',
                'categoria': article.categoria.nome if article.categoria else '',
                'autor': article.autor.username if article.autor else '',
            })
        
        return JsonResponse({'articles': articles_data})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)


'''


class ArticlesByCategoryView(ListView):
    """Class-based view to get articles filtered by category"""
    model = Artigo
    context_object_name = 'articles'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.request.GET.get('category', '').lower()
        
        if category_name:
            return Artigo.objects.filter(
                categoria__nome__iexact=category_name
            ).order_by('-data_publicacao')
        return Artigo.objects.all().order_by('-data_publicacao')

    def render_to_response(self, context, **response_kwargs):
        if self.request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            articles_data = []
            for article in context['articles']:
                articles_data.append({
                    'id': article.id,
                    'titulo': article.titulo,
                    'conteudo': article.conteudo[:200] + '...' if len(article.conteudo) > 200 else article.conteudo,
                    'data_publicacao': article.data_publicacao.strftime('%b %d, %Y'),
                    'views': article.views,
                    'image_url': article.image.url if article.image else '',
                    'categoria': article.categoria.nome if article.categoria else '',
                    'autor': article.autor.username if article.autor else '',
                })
            return JsonResponse({'articles': articles_data})
        
        return JsonResponse({'error': 'Invalid request'}, status=400)





        

    






       
   

   
        
            
           




    

    


   









    

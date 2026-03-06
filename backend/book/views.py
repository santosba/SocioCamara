from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from .serializers import BookSerializer
from django.forms import ModelForm
from .form import BookForm

from .models import Book
from django.template.loader import get_template

class BookListView(ListView):
    template_name = 'book/book_list.html'
    model = Book
    queryset = Book.objects.all()
    context_object_name ='books'
    login_url = 'login'



class createBookview(CreateView):
    model = Book
    template_name = 'book/book_form.html'
    form_class = BookForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
   

class BookDetailView(DetailView):
    model = Book
    template_name = 'book/book_detail.html'
    queryset = Book.objects.all()
    login_url = 'login'

    def get_object(self):
        id_ = self.kwargs.get('id')
        return get_object_or_404(Book, id=id_)

   

    




from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import BookListView, BookDetailView, createBookview

class BookURLTests(SimpleTestCase):
    def test_book_list_url(self):
        url = reverse('book:book-list')
        self.assertEqual(resolve(url).func.view_class, BookListView)

    def test_book_detail_url(self):
        url = reverse('book:detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, BookDetailView)

    def test_create_book_url(self):
        url = reverse('book:new')
        self.assertEqual(resolve(url).func.view_class, createBookview)
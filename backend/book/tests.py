from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth import get_user_model
from .views import BookListView, BookDetailView, createBookview
from .models import Book, BookReview

class BookTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username='reviewuser',
            email='reviewuser@example.com',
            password='testpassword'
        )

        cls.book = Book.objects.create(
            title='Test Book',
            author='Test Author',
            price=19.99,  
            published='2023-01-01'
        )

        cls.review = BookReview.objects.create(
            book=cls.book,
            review='This is a test review.',
            rating=5,
            author=cls.user
        )
    def test_book_listing(self):
        response = self.client.get(reverse('book:book-list'))
        self.assertEqual(f"{self.book.title}", 'Test Book')
        self.assertEqual(f"{self.book.author}", 'Test Author')
        self.assertTemplateUsed(response, 'book/book_list.html')
        self.assertEqual(f"{self.book.price}", '19.99')

    def test_book_list_view(self):
        response = self.client.get(reverse('book:book-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_list.html')
       


    def test_book_detail_view(self):
        response = self.client.get(reverse('book:book-detail', args=[self.book.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book/book_detail.html')
       
       

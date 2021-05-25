from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('books', views.books, name='books'),
    path('books/<int:book_id>/<slug:book_title_slug>', views.bookSingle, name='book-single')
]

from django.urls import path
from . import views

app_name = 'Books'

urlpatterns = [
    path('', views.books, name='books'),
    path('<int:book_id>/<slug:book_title_slug>', views.bookSingle, name='book-single')
]

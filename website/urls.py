from django.urls import path
from . import views


app_name = 'website'

urlpatterns = [
    path('', views.home, name='home'),
    path('about-us', views.aboutUs, name='aboutUs'),
    path('books', views.books, name='books'),
    path('books/book-title-slug', views.bookSingle, name='book-single'),
    path('blogs', views.blogs, name='blogs'),
    path('blogs/blog-title-slug', views.blogSingle, name='blog-single'),
    path('contact', views.contact, name='contact')
]

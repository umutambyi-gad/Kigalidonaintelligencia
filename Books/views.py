from django.shortcuts import render
from Contact.views import footerContacts
from .models import (
    Books,
    Categories
)


# Create your views here.
def books(request):
    books = Books.objects.all()
    categories = Categories.objects.all()
    context = {
        'books': books,
        'categories': categories
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'books.html', context=context)


def bookSingle(request, book_id, book_title_slug):
    book = Books.objects.get(pk=book_id)
    recent_books = Books.recent_books()
    popular_books = Books.popular_books()
    categories = Categories.objects.all()

    if request.method == 'GET':
        views = book.views + 1
        book.views = views
        book.save()

    context = {
        'popular_books': popular_books,
        'recent_books': recent_books,
        'book': book,
        'categories': categories
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'book-single.html', context=context)


def searchBook(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        category = request.GET.get('cat')

        result = ''

        if category == 'all-category':
            result = Books.search_book(
                query=query
            )
        else:
            result = Books.search_book_with_category(
                category=category,
                query=query
            )

    categories = Categories.objects.all()

    context = {
        'categories': categories,
        'query': query,
        'category': category,
        'books': result
    }

    context = {**context, **footerContacts(request)}

    return render(request, 'book-result-page.html', context=context)


def newBook(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'new-book.html', context=context)

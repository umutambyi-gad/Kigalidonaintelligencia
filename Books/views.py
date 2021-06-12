from django.shortcuts import render
from Contact.views import footerContacts
from .models import Books


# Create your views here.
def books(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'books.html', context=context)

def bookSingle(request, book_id, book_title_slug):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'book-single.html', context=context)

def newBook(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'new-book.html', context=context)

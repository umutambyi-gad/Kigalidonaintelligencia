from django.shortcuts import render
from Contact.views import footerContacts

# Create your views here.
def books(request):
    context = {}
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

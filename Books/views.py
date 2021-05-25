from django.shortcuts import render


# Create your views here.
def books(request):
    return render(request, 'books.html')

def bookSingle(request, book_id, book_title_slug):
    return render(request, 'book-single.html')

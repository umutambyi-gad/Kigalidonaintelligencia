from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def books(request):
    return render(request, 'books.html')

def bookSingle(request, book_id, book_title_slug):
    return render(request, 'book-single.html')

def blogs(request):
    return render(request, 'blogs.html')

def blogSingle(request, blog_id, blog_title_slug):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

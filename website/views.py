from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'index.html')

def aboutUs(request):
    return render(request, 'about-us.html')

def books(request):
    return render(request, 'books.html')

def bookSingle(request):
    return render(request, 'book-single.html')

def blogs(request):
    return render(request, 'blogs.html')

def blogSingle(request):
    return render(request, 'blog-single.html')

def contact(request):
    return render(request, 'contact.html')

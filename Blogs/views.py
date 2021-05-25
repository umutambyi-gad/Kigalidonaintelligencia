from django.shortcuts import render


# Create your views here.
def blogs(request):
    return render(request, 'blogs.html')

def blogSingle(request, blog_id, blog_title_slug):
    return render(request, 'blog-single.html')

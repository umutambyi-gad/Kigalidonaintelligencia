from django.shortcuts import render
from Contact.views import footerContacts
from .models import Blogs


# Create your views here.
def blogs(request):
    blogs = Blogs.objects.all()
    context = {
        'blogs': blogs
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'blogs.html', context=context)

def blogSingle(request, blog_id, blog_title_slug):
    current_blog = Blogs.objects.get(pk=blog_id)

    if request.method == 'GET':
        views = current_blog.views + 1
        current_blog.views = views
        current_blog.save()

    context = {
        'blog': current_blog,
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'blog-single.html', context=context)

def newBlog(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'new-blog.html', context=context)

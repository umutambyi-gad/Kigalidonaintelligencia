from django.shortcuts import render
from Contact.views import footerContacts
from .models import (
    Blogs,
    Categories
)


# Create your views here.
def blogs(request):
    blogs = Blogs.objects.all()
    categories = Categories.objects.all()
    context = {
        'blogs': blogs,
        'categories': categories,
    }
    context = {**context, **footerContacts(request)}
    return render(request, 'blogs.html', context=context)

def searchBlog(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        category = request.GET.get('cat')

        result = ''

        if category == 'all-category':
            result = Blogs.search_blog(
                query=query
            )
        else:
            result = Blogs.search_blog_with_category(
                category=category,
                query=query
            )

    categories = Categories.objects.all()

    context = {
        'query': query,
        'category': category,
        'categories': categories,
        'blogs': result
    }

    context = {**context, **footerContacts(request)}

    return render(request, 'blog-result-page.html', context=context)


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

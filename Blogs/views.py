from django.shortcuts import render
from Contact.views import footerContacts


# Create your views here.
def blogs(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'blogs.html', context=context)

def blogSingle(request, blog_id, blog_title_slug):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'blog-single.html', context=context)

def newBlog(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'new-blog.html', context=context)

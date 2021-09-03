from django.shortcuts import render
from Contact.views import footerContacts
from django.http import JsonResponse
from .models import (
    Blogs,
    Categories,
    RootComments,
    ReplyComments
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
    categories = Categories.objects.all()

    if request.method == 'GET':
        views = current_blog.views + 1
        current_blog.views = views
        current_blog.save()

    context = {
        'blog': current_blog,
        'categories': categories
    }

    if request.is_ajax():
        root_comment_id = int(request.POST['root_comment_id'])
        commentor = request.POST['commentor']
        comment = request.POST['comment']

        if root_comment_id == 0:
            new_root_comment = RootComments.objects.create(
                commentor=commentor,
                comment=comment,
                blog_id=blog_id
            )

            return JsonResponse(
                {
                    'is_root': True,
                    'comment_id': new_root_comment.pk,
                    'time_t': new_root_comment.added_date.strftime("%Y-%m-%d"),
                    'time_b': new_root_comment.added_date.strftime("%b %d, %Y"),
                    'commentor': new_root_comment.commentor,
                    'comment': new_root_comment.comment
                },status=200
            )

        else:
            new_reply_comment = ReplyComments.objects.create(
                reply_commentor=commentor,
                reply_comment=comment,
                root_comment_id=root_comment_id,
                blog_id=blog_id
            )
            return JsonResponse(
                {
                    'is_root': False,
                    'root_comment_id': new_reply_comment.root_comment_id,
                    'time_t': new_reply_comment.added_date.strftime("%Y-%m-%d"),
                    'time_b': new_reply_comment.added_date.strftime("%b %d, %Y"),
                    'commentor': new_reply_comment.reply_commentor,
                    'comment': new_reply_comment.reply_comment
                },status=200
            )

    context = {**context, **footerContacts(request)}
    return render(request, 'blog-single.html', context=context)

def newBlog(request):
    context = {}
    context = {**context, **footerContacts(request)}
    return render(request, 'new-blog.html', context=context)

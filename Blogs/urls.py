from django.urls import path
from . import views


app_name = 'Blogs'

urlpatterns = [
    path('', views.blogs, name='blogs'),
    path('<int:blog_id>/<slug:blog_title_slug>', views.blogSingle, name='blog-single'),
    path('new-blog', views.newBlog, name='new-blog'),
]

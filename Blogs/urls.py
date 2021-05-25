from django.urls import path
from . import views


app_name = 'Blogs'

urlpatterns = [
    path('blogs', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>/<slug:blog_title_slug>', views.blogSingle, name='blog-single'),
]

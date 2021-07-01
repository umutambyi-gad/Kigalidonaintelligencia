from django.db import models
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
from django.template.defaultfilters import slugify
from django.shortcuts import reverse


# Create your models here.
class Tags(models.Model):
	tag = models.CharField(max_length=150)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag

	class Meta:
		verbose_name_plural = 'Tags'


class Categories(models.Model):
	category = models.CharField(max_length=150)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'Categories'



class Blogs(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    description = models.TextField()
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='media/blogs/images')
    author_comment = models.TextField()
    related_tags = models.ManyToManyField(Tags)
    related_categories = models.ManyToManyField(Categories)
    first_image = models.ImageField(upload_to='media/blogs/images', null=True, blank=True)
    second_image = models.ImageField(upload_to='media/blogs/images', null=True, blank=True)
    third_image = models.ImageField(upload_to='media/blogs/images', null=True, blank=True)
    fourth_image = models.ImageField(upload_to='media/blogs/images', null=True, blank=True)
    fifth_image = models.ImageField(upload_to='media/blogs/images', null=True, blank=True)
    views = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse("Blogs:blog-single", args=[str(self.id), str(self.slug())])
    
    @classmethod
    def recent_blogs(cls):
        recents = cls.objects.order_by('-added_date')
        return recents[:3]
    
    def __str__(self):
        return self.title

    @classmethod
    def search_blog(cls, query):
        result = cls.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author_comment__icontains=query) |
            Q(content__icontains=query)
        )

        return result

    @classmethod
    def search_blog_with_category(cls, category, query):
        result = cls.objects.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query) |
            Q(author_comment__icontains=query) |
            Q(content__icontains=query) |
            Q(related_categories=Categories.objects.get(category=category))
        )

        return result

    class Meta:
        verbose_name_plural = 'Blogs'


class RootComments(models.Model):
    commentor = models.CharField(max_length=255)
    comment = models.TextField()
    blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.commentor

    class Meta:
        verbose_name_plural = 'Root Comments'


class ReplyComments(models.Model):
    reply_commentor = models.CharField(max_length=255)
    reply_comment = models.TextField()
    root_comment = models.ForeignKey(RootComments, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.reply_commentor
	
    class Meta:
        verbose_name_plural = 'Reply Comments'

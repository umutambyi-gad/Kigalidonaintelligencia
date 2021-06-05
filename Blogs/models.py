from django.db import models
from django.contrib.auth.models import User
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
    author = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
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
    views = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.title)

    def get_absolute_url(self):
        return reverse("Blogs:blogSingle", args=[str(self.id), str(self.slug())])
    
    @classmethod
    def recent_blog(cls):
        recents = cls.objects.order_by('-added_date')
        return recents[:3]
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Blogs'
    
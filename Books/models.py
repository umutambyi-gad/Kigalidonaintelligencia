from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.shortcuts import reverse


# Create your models here.
class Categories(models.Model):
	category = models.CharField(max_length=150)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'Categories'


class Books(models.Model):
    athour = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='media/books/images', null=True, blank=True)
    short_summary = models.TextField()
    long_summary = models.TextField()
    related_tags = models.ManyToManyField(Categories)
    views = models.IntegerField(default=0)
    added_date = models.DateTimeField(auto_now_add=True)

    def slug(self):
        return slugify(self.name)

    def get_absolute_url(self):
        return reverse("Books:book-single", args=[str(self.id), str(self.slug())])
    
    @classmethod
    def recent_books(cls):
        recents = cls.objects.order_by('-added_date')
        return recents[:9]
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Books'

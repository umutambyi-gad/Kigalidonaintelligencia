from django.db import models
from django.contrib.auth.models import User
from django.db.models.query_utils import Q
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
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    edition = models.CharField(max_length=255)
    ISBN = models.CharField(max_length=255)
    publisher = models.CharField(max_length=255)
    thumbnail = models.ImageField(upload_to='media/books/images', null=True, blank=True)
    short_summary = models.TextField()
    long_summary = models.TextField()
    related_category = models.OneToOneField(Categories, on_delete=models.CASCADE)
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

    @classmethod
    def search_book(cls, query):
        result = cls.objects.filter(
            Q(name__icontains=query) |
            Q(edition__icontains=query) |
            Q(short_summary__icontains=query) |
            Q(long_summary__icontains=query)
        )

        return result
    
    @classmethod
    def search_book_with_category(cls, category, query):
        result = cls.objects.filter(
            Q(name__icontains=query) |
            Q(edition__icontains=query) |
            Q(short_summary__icontains=query) |
            Q(long_summary__icontains=query) |
            Q(related_category=Categories.objects.get(category=category))
        )

        return result
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Books'

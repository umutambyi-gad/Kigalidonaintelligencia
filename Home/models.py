from django.db import models


# Create your models here.
class HomeBackground(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/home/images')
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.background_title
    class Meta:
        verbose_name_plural = 'Home background section'


class HomeWelcoming(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/home/images')
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'Home welcoming section'


class TestimonyAdding(models.Model):
    author_name = models.CharField(max_length=255)
    author_email = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='media/home/images')
    testimony = models.TextField()
    linkedin_profile = models.CharField(max_length=255)
    facebook_profile = models.CharField(max_length=255)
    twitter_profile = models.CharField(max_length=255)
    instagram_profile = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.author_name
    
    class Meta:
        verbose_name_plural = 'Testimony Adding Section'

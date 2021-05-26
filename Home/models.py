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

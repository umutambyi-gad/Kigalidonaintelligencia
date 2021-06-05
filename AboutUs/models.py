from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/home/images')
    description = models.TextField()
    added_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if AboutUs.objects.count() > 0:
            return False
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'About us section'


class SocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_profile = models.CharField(max_length=255, null=True, blank=True)
    facebook_profile = models.CharField(max_length=255, null=True, blank=True)
    twitter_profile = models.CharField(max_length=255, null=True, blank=True)
    instagram_profile = models.CharField(max_length=255, null=True, blank=True)
    youtube_profile = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if AboutUs.objects.count() > 0:
            return False
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Social media'

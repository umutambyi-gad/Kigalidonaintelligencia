from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'contacts'

class SocialMedia(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    linkedin_profile = models.CharField(max_length=255, null=True, blank=True)
    facebook_profile = models.CharField(max_length=255, null=True, blank=True)
    twitter_profile = models.CharField(max_length=255, null=True, blank=True)
    instagram_profile = models.CharField(max_length=255, null=True, blank=True)
    youtube_profile = models.CharField(max_length=255, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        if SocialMedia.objects.count() > 0:
            return False
        
        super().save(*args, **kwargs)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name_plural = 'Social media'

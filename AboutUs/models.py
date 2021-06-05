from django.db import models

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

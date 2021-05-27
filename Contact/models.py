from django.db import models

# Create your models here.
class Contact(models.Model):
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'contacts'

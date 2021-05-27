from django.contrib import admin
from .models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('phone', 'email', 'address')
		}),
	)
	list_display = ('address', 'added_date')

admin.site.register(Contact, ContactAdmin)

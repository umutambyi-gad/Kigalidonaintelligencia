from django.contrib import admin
from .models import (
	Contact,
	SocialMedia
)


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('phone', 'email', 'address')
		}),
	)
	list_display = ('address', 'added_date')

admin.site.register(Contact, ContactAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
	fieldsets = (
		('Social media profiles', {
			'fields': ('linkedin_profile', 'facebook_profile', 'twitter_profile', 'instagram_profile', 'youtube_profile')
		}),
	)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		return super().save_model(request, obj, form, change)

	list_display = ('user', 'added_date')

admin.site.register(SocialMedia, SocialMediaAdmin)

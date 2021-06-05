from django.contrib import admin
from .models import (
	AboutUs,
	SocialMedia
)


# Register your models here.
class AboutUsAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('title', 'description')
		}),
	('Image section', {
		'fields': ('image', )
		})
	)
	list_display = ('title', 'added_date')

admin.site.register(AboutUs, AboutUsAdmin)


class SocialMediaAdmin(admin.ModelAdmin):
	fieldsets = (
		('Social media profiles', {
			'fields': ('linkedin_profile', 'facebook_profile', 'twitter_profile', 'instagram_profile', 'youtube_profile')
		}),
	)
	list_display = ('user', 'added_date')

admin.site.register(SocialMedia, SocialMediaAdmin)

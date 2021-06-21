from django.contrib import admin
from .models import (
    HomeBackground,
    HomeWelcoming,
	TestimonyAdding
)

admin.site.site_header = 'Intelligencia Administration'
admin.site.site_title = admin.site.site_header

# Register your models here.
class HomeBackgroundAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'description')
		}),
		('Image section', {
			'fields': ('image', )
		})
	)
	list_display = ('title', 'added_date')

admin.site.register(HomeBackground, HomeBackgroundAdmin)


class HomeWelcomingAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'description')
		}),
		('Image section', {
			'fields': ('image', )
		})
	)
	list_display = ('title', 'added_date')

admin.site.register(HomeWelcoming, HomeWelcomingAdmin)


class TestimonyAddingAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('author_name', 'author_email', 'testimony')
		}),
		('Image section', {
			'fields': ('author_image', )
		}),
		('Social media section', {
			'fields': ('linkedin_profile', 'facebook_profile', 'twitter_profile', 'instagram_profile')
		})
	)
	list_display = ('author_name', 'added_date')

admin.site.register(TestimonyAdding, TestimonyAddingAdmin)

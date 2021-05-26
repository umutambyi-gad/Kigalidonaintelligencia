from django.contrib import admin
from .models import (
    HomeBackground,
    HomeWelcoming
)


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

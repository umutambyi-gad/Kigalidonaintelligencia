from django.contrib import admin
from .models import AboutUs


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

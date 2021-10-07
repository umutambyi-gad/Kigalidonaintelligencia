from django.contrib import admin
from .models import (
    Categories,
    Books
)


# Register your models here.
class CategoriesAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('category',)
		}),
		
	)
	list_display = ('category', 'added_date')

admin.site.register(Categories, CategoriesAdmin)

class BooksAdmin(admin.ModelAdmin):
    fieldsets = (
		('Book informations', {
			'fields': ('name', 'edition', 'ISBN', 'publisher', 'views', 'link')
		}),
        ('Book thumbnail (Optional)', {
			'fields': ('thumbnail',)
		}),
        ('Book summary', {
			'fields': ('summary',)
		}),
        ('Related', {
            'fields': ('related_category',)
        })
    )

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)

    list_display = ('name', 'added_date')

admin.site.register(Books, BooksAdmin)

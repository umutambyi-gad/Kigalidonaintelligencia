from django.contrib import admin
from .models import (
    Categories,
    Tags,
    Blogs
)


# Register your models here.
class TagsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('tag',)
		}),
		
	)
	list_display = ('tag', 'added_date')

admin.site.register(Tags, TagsAdmin)


class CategoriesAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('category',)
		}),
		
	)
	list_display = ('category', 'added_date')

admin.site.register(Categories, CategoriesAdmin)


class BlogsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'description', 'content', 'author_comment', 'related_tags', 'related_categories')
		}),
        ('Image section (Required)', {
            'fields': ('thumbnail', )
        }),
        ('Image section (Optional)', {
			'fields': ('first_image', 'second_image', 'third_image', 'fourth_image', 'fifth_image')
		}),
	)

	def save_model(self, request, obj, form, change):
		obj.author = request.user
		super().save_model(request, obj, form, change)

	list_display = ('title', 'added_date')

admin.site.register(Blogs, BlogsAdmin)

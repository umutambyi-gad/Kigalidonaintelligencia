from django.contrib import admin
from .models import (
    Tags,
    Blogs
)


# Register your models here.
class TagsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('tag', 'added_date')
		}),
		
	)
	list_display = ('tag', 'added_date')

admin.site.register(Tags, TagsAdmin)


class BlogsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('author', 'title', 'description', 'content', 'author_comment', 'related_tag')
		}),
        ('Image section (Required)', {
            'fields': ('thumbnail', )
        }),
        ('Image section (Optional)', {
			'fields': ('first_image', 'second_image', 'third_image', 'fourth_image', 'fifth_image')
		}),
	)
	list_display = ('author', 'added_date')

admin.site.register(Blogs, BlogsAdmin)

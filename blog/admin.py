from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Info', {'fields': ['author']}),
        ('context', {'fields': ['title', 'content', ]}),
        ('time', {'fields': ['post_date']}),

    ]
    list_display = ('title','author','post_date')
    list_filter = ['post_date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)

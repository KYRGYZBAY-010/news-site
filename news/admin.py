from atexit import register
from django.contrib import admin
from .models import Articles

class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title' )
    list_display_links = ('id', 'title')


admin.site.register(Articles, ArticlesAdmin)

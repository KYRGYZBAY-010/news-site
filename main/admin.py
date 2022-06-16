from django.contrib import admin

from .models import HomeNews, About

class HomeNewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date')
    list_display_links = list_display


admin.site.register(HomeNews, HomeNewsAdmin)
admin.site.register(About)

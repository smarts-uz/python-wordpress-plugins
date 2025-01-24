from django.contrib import admin
from .models import wordpres_org

@admin.register(wordpres_org)
class PluginAdmin(admin.ModelAdmin):
    list_display = ['slug', 'name', 'fivestars', 'last_updated', 'tested']
    search_fields = ['slug', 'name']
    list_filter = ['tested', 'ratings']
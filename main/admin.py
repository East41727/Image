from django.contrib import admin
from .models import GalleryModel



@admin.register(GalleryModel)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    readonly_fields = ['created','updated']
    fields = ['name', 'slug', 'description','image','created','updated'] 
    



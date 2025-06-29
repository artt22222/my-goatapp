from django.contrib import admin
from app_goat.models import Diseases
# Register your models here.


class DiseasesAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']
    
admin.site.register(Diseases, DiseasesAdmin)
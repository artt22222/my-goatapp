from django.contrib import admin
from app_goat.models import Diseases,GoatStatistics
# Register your models here.


class DiseasesAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']
    
admin.site.register(Diseases, DiseasesAdmin)

@admin.register(GoatStatistics)
class GoatStatisticsAdmin(admin.ModelAdmin):
    list_display = ('total_goats', 'total_farmers', 'goats_south', 'farmers_south', 'updated_at')
    readonly_fields = ('updated_at',)
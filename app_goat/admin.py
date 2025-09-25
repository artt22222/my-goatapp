from django.contrib import admin
from app_goat.models import Diseases,GoatStatistics
# Register your models here.

# ====== เปลี่ยนชื่อ Django Admin ======
admin.site.site_header = "การจัดการ DGOAT"
admin.site.index_title = "เมนูหลักการจัดการ DGOAT"
# =====================================

class DiseasesAdmin(admin.ModelAdmin):
    list_display = ['title','image']
    search_fields = ['title']
    
admin.site.register(Diseases, DiseasesAdmin)

@admin.register(GoatStatistics)
class GoatStatisticsAdmin(admin.ModelAdmin):
    list_display = ('total_goats', 'total_farmers', 'goats_south', 'farmers_south', 'updated_at')
    readonly_fields = ('updated_at',)
from django.db import models

class Diseases(models.Model):
    title = models.CharField(max_length=50)
    cause = models.TextField(default="เพิ่มข้อมูล", blank=True, null=True)
    symptom = models.TextField(default="เพิ่มข้อมูล", blank=True, null=True)
    treatment = models.TextField(default="เพิ่มข้อมูล", blank=True, null=True)
    image = models.ImageField(upload_to='disease_images/', blank=True, null=True)

    def __str__(self):
        return '{} (id={})'.format(self.title, self.id)
    
class GoatStatistics(models.Model):
    total_goats = models.PositiveIntegerField("ประชากรแพะในประเทศไทย", default=0)
    total_farmers = models.PositiveIntegerField("เกษตรกรในประเทศไทย", default=0)
    goats_south = models.PositiveIntegerField("ประชากรแพะในสามจังหวัดชายแดนใต้", default=0)
    farmers_south = models.PositiveIntegerField("เกษตรกรในสามจังหวัดชายแดนใต้", default=0)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "ข้อมูลสถิติแพะ"
        verbose_name_plural = "ข้อมูลสถิติแพะ"

    def __str__(self):
        return f"อัปเดตเมื่อ {self.updated_at.strftime('%d/%m/%Y %H:%M')}"    
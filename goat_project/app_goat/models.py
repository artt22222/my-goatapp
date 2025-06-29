from django.db import models

# Create your models here.

class Diseases(models.Model):
    title = models.CharField(max_length=50)
    cause = models.TextField(default=False)
    sympton = models.TextField(default=False)
    treatment = models.TextField(default=False)
    image = models.ImageField(upload_to='disease_images/',blank=True,null=True)
    
    
    def __str__(self):
        return '{} (id={})'.format(self.title, self.id)
    
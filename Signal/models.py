
from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name_plural = 'Categories'
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000,)
    def __str__(self):
         return self.name

class Signal(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200,)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    colour = models.CharField(null = True, blank = True, max_length=200)
    flash_type = models.CharField(null = True, blank = True, max_length=200)
    image = models.ImageField(
        null=True, 
        blank=True, 
        upload_to='', 
        default='placeholder.png'
        )
    def __str__(self):
         return self.title


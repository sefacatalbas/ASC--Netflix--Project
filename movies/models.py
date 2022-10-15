from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models

# Create your models here.
class Kategori(models.Model):
    isim = models.CharField(max_length=100)

    def __str__(self):
        return self.isim
class Movie(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.CASCADE, null=True)
    isim = models.CharField(max_length=200)
    resim = models.FileField(upload_to='filmler/', verbose_name='Film ismi')
    video = models.FileField(upload_to ="videolar/", null= True, blank = True)
    def __str__(self):
        return self.isim
        
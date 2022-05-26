from django.db import models

# Create your models here.
class Tariff(models.Model):
    tariffFile = models.FileField(verbose_name='Excel файл сделанный по шаблону',upload_to='static/files')

    def __str__(self):
        return 'Файл тариффа'

    class Meta:
        verbose_name = "Файл тарифа"
        verbose_name_plural = "Файл тарифа"
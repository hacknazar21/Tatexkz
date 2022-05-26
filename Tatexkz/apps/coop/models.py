from datetime import datetime
from django.db import models

# Create your models here.


class Coop(models.Model):
    name = models.CharField(max_length=30, verbose_name='ФИО')
    tel = models.CharField(max_length=15, verbose_name='Контактный телефон')
    email = models.EmailField(verbose_name="E-Mail")
    company = models.CharField(max_length=100, verbose_name="Название компании")
    services = models.CharField(max_length=100, verbose_name="Услуги")
    volume = models.CharField(max_length=1000000, verbose_name="Ожидаемый объем отправлений (шт в месяц)")
    cargo = models.CharField(max_length=1000000, verbose_name="Характер груза")
    geo = models.CharField(max_length=100, verbose_name="География отправок")
    date = models.DateTimeField(verbose_name='Дата и время подачи заявки', blank=True, default=datetime.now)
    
    def __str__(self):
        return self.geo
    
    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"

class CoopSettings(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=10000, verbose_name='Текст')
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Настройки сотрудничества"
        verbose_name_plural = "Настройки сотрудничества"
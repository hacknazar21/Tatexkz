from django.db import models

# Create your models here.


class Promo(models.Model):
    promo = models.CharField(max_length=30, null=True, verbose_name='Промокод')
    datefrom = models.DateTimeField(null=True, verbose_name='Срок начала')
    dateto = models.DateTimeField(null=True, verbose_name='Срок конца')
    percent = models.IntegerField(null=True, verbose_name='Процент снижения')

    def __str__(self):
        return self.promo

    class Meta:
        verbose_name = "Промокод"
        verbose_name_plural = "Промокоды"

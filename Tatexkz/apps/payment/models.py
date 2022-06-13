from datetime import datetime
from django.db import models
from django.utils import timezone
# Create your models here.


class Order(models.Model):
    typePackage = models.CharField(max_length=30, verbose_name='Тип посылки')
    trackcode = models.CharField(max_length=16,
                                 verbose_name='Номер накладной', default='0000000000', blank=True)
    courierNum = models.CharField(max_length=16,
                                 verbose_name='Номер подтверждения', blank=True)
    date = models.CharField(
        max_length=50, verbose_name='Время подтверждения', null=True, blank=True)
    weight = models.FloatField(max_length=30, verbose_name='Вес')
    sendersName = models.CharField(
        max_length=100, verbose_name='Имя отправителя')
    recipientName = models.CharField(
        max_length=100, verbose_name='Имя получателя')
    fromCity = models.CharField(
        max_length=100, verbose_name='Город отправителя')
    whereCity = models.CharField(
        max_length=100, verbose_name='Город получателя')
    fromCountry = models.CharField(
        max_length=100, verbose_name='Страна отправителя')
    whereCountry = models.CharField(
        max_length=100, verbose_name='Страна отправителя')
    length = models.CharField(
        max_length=100, null=True, verbose_name='Длина посылки')
    width = models.CharField(null=True, max_length=100,
                             verbose_name='Ширина посылки')
    height = models.CharField(
        max_length=100, null=True, verbose_name='Высота посылки')
    sendersAddress = models.CharField(
        max_length=1000, verbose_name='Адрес отправителя')
    recipientAddress = models.CharField(
        max_length=1000, verbose_name='Адрес получателя')
    postIndexSender = models.CharField(
        max_length=6, verbose_name='Почтовый индекс отправителя')
    postIndexRecipient = models.CharField(
        max_length=6, verbose_name='Почтовый индекс получателя')
    dataSend = models.CharField(
        max_length=30, verbose_name='Дата забора')
    sendersTel = models.CharField(
        max_length=30, verbose_name='Телефон отправителя')
    recipientTel = models.CharField(
        max_length=30, verbose_name='Телефон получателя')
    email = models.EmailField(max_length=30, verbose_name='Email')
    comment = models.TextField(
        max_length=300, null=True, verbose_name='Подробное содержимое груза', blank=True)
    instruction = models.TextField(
        max_length=300, null=True, verbose_name='Инструкция для курьера', blank=True)
    printNeed = models.BooleanField(null=True, verbose_name='Печать')
    apply = models.BooleanField(
        verbose_name='Подтвердить', default=False, null=True)
    invoiceID = models.IntegerField(default=0, blank=True, editable=False)
    shipmentDate = models.TimeField(
        verbose_name='Раннее время', default=timezone.now)
    shipmentDateFuture = models.TimeField(
        verbose_name='Позднее время', default=timezone.now)
    isPay = models.BooleanField(
        verbose_name='Оплачено', default=False)
    
    def __str__(self):
        return self.sendersName

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"

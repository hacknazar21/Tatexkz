# Generated by Django 4.0.3 on 2022-06-08 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0017_order_ispay_alter_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipmentDate',
            field=models.TimeField(blank=True, verbose_name='Дата и время передачи в DHL'),
        ),
    ]
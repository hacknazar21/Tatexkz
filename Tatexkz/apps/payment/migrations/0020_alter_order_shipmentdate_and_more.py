# Generated by Django 4.0.3 on 2022-06-08 10:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0019_order_shipmentdatefuture_alter_order_shipmentdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipmentDate',
            field=models.TimeField(verbose_name='Раннее время'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shipmentDateFuture',
            field=models.TimeField(default=django.utils.timezone.now, verbose_name='Позднее время'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-20 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_order_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='apply',
            field=models.BooleanField(default=False, null=True, verbose_name='Подтвердить'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.CharField(default='01-01-2022 00:00', max_length=30, verbose_name='Время подтверждения'),
        ),
        migrations.AlterField(
            model_name='order',
            name='trackcode',
            field=models.IntegerField(default='0000000000', verbose_name='Номер накладной'),
        ),
    ]

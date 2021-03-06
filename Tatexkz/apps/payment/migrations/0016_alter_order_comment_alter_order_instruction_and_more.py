# Generated by Django 4.0.3 on 2022-05-23 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_alter_order_postindexrecipient_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Подробное содержимое груза'),
        ),
        migrations.AlterField(
            model_name='order',
            name='instruction',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='Инструкция для курьера'),
        ),
        migrations.AlterField(
            model_name='order',
            name='trackcode',
            field=models.CharField(blank=True, default='0000000000', max_length=10, verbose_name='Номер накладной'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-20 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0009_alter_order_trackcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='trackcode',
            field=models.CharField(default='0000000000', max_length=10, verbose_name='Номер накладной'),
        ),
    ]

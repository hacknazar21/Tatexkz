# Generated by Django 4.0.3 on 2022-04-20 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_order_trackcode_alter_order_apply_alter_order_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date',
            field=models.DateTimeField(
                null="True", verbose_name='Время подтверждения'),
        ),
    ]

# Generated by Django 4.0.3 on 2022-05-19 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0010_alter_order_trackcode'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='invoiceID',
            field=models.IntegerField(blank=True, default=0, editable=False),
        ),
    ]

# Generated by Django 4.0.3 on 2022-04-21 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('promo', '0002_alter_promo_datefrom_alter_promo_dateto_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='promo',
            old_name='procent',
            new_name='percent',
        ),
    ]

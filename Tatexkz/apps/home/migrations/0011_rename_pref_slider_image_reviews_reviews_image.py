# Generated by Django 4.0.3 on 2022-05-19 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_reviews_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviews',
            old_name='pref_slider_image',
            new_name='reviews_image',
        ),
    ]

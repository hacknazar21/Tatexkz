# Generated by Django 4.0.3 on 2022-05-27 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0016_pref_slider_pref_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pref_slider',
            name='pref_title',
        ),
    ]
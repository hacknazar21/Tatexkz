# Generated by Django 4.0.3 on 2022-05-19 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_about_options_alter_about_about_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='about_text',
            field=models.TextField(max_length=10000, verbose_name='Текст О нас'),
        ),
    ]
# Generated by Django 4.0.3 on 2022-05-27 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_text_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Текст слайда'),
        ),
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_text_kz',
            field=models.CharField(max_length=50, null=True, verbose_name='Текст слайда'),
        ),
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_text_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Текст слайда'),
        ),
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_title_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_title_kz',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок слайда'),
        ),
        migrations.AddField(
            model_name='main_slider',
            name='main_slider_title_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Заголовок слайда'),
        ),
    ]

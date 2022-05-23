# Generated by Django 4.0.3 on 2022-05-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_alter_about_about_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pref_Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pref_slider_title', models.CharField(max_length=50, verbose_name='Заголовок слайда')),
                ('pref_slider_text', models.TextField(max_length=100, verbose_name='Текст слайда')),
                ('pref_slider_image', models.ImageField(upload_to='static/img/first-screen', verbose_name='Картинка слайда')),
            ],
            options={
                'verbose_name': 'Слайд преимущества',
                'verbose_name_plural': 'Слайды преимущества',
            },
        ),
    ]
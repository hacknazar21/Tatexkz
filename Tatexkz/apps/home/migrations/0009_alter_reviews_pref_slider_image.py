# Generated by Django 4.0.3 on 2022-05-19 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_reviews_alter_about_about_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='pref_slider_image',
            field=models.ImageField(upload_to='static/img/reviews', verbose_name='Картинка отзыва'),
        ),
    ]

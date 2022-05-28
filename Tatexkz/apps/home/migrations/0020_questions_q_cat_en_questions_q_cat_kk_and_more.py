# Generated by Django 4.0.3 on 2022-05-27 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0019_alter_pref_options_pref_pref_title_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='q_cat_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_cat_kk',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_cat_ru',
            field=models.CharField(max_length=50, null=True, verbose_name='Категория вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_text_en',
            field=models.TextField(max_length=5000, null=True, verbose_name='Текст вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_text_kk',
            field=models.TextField(max_length=5000, null=True, verbose_name='Текст вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_text_ru',
            field=models.TextField(max_length=5000, null=True, verbose_name='Текст вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_title_en',
            field=models.TextField(max_length=50, null=True, verbose_name='Заголовок вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_title_kk',
            field=models.TextField(max_length=50, null=True, verbose_name='Заголовок вопроса'),
        ),
        migrations.AddField(
            model_name='questions',
            name='q_title_ru',
            field=models.TextField(max_length=50, null=True, verbose_name='Заголовок вопроса'),
        ),
    ]

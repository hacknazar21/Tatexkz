# Generated by Django 4.0.3 on 2022-05-25 14:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='ФИО')),
                ('tel', models.CharField(max_length=15, verbose_name='Контактный телефон')),
                ('email', models.EmailField(max_length=254, verbose_name='E-Mail')),
                ('company', models.CharField(max_length=100, verbose_name='Название компании')),
                ('services', models.CharField(max_length=100, verbose_name='Услуги')),
                ('volume', models.CharField(max_length=1000000, verbose_name='Ожидаемый объем отправлений (шт в месяц)')),
                ('cargo', models.CharField(max_length=1000000, verbose_name='Ожидаемый объем отправлений (шт в месяц)')),
                ('geo', models.CharField(max_length=100, verbose_name='Ожидаемый объем отправлений (шт в месяц)')),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now, verbose_name='Дата и время подачи заявки')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
            },
        ),
    ]

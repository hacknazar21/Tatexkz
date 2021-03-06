# Generated by Django 4.0.3 on 2022-05-26 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coop', '0002_alter_coop_cargo_alter_coop_geo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoopSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.CharField(max_length=100, verbose_name='Текст')),
            ],
            options={
                'verbose_name': 'Настройки сотрудничества',
                'verbose_name_plural': 'Настройки сотрудничества',
            },
        ),
    ]

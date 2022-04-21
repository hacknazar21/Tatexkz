# Generated by Django 4.0.3 on 2022-04-15 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typePackage', models.CharField(max_length=30)),
                ('weight', models.FloatField(max_length=30)),
                ('sendersName', models.CharField(max_length=30)),
                ('recipientName', models.CharField(max_length=30)),
                ('fromCity', models.CharField(max_length=30)),
                ('whereCity', models.CharField(max_length=30)),
                ('fromCountry', models.CharField(max_length=30)),
                ('whereCountry', models.CharField(max_length=30)),
                ('length', models.IntegerField(max_length=100, null=True)),
                ('width', models.IntegerField(max_length=100, null=True)),
                ('height', models.IntegerField(max_length=100, null=True)),
                ('sendersAddress', models.CharField(max_length=30)),
                ('recipientAddress', models.CharField(max_length=30)),
                ('postIndexSender', models.CharField(max_length=30)),
                ('postIndexRecipient', models.CharField(max_length=30)),
                ('dataSend', models.CharField(max_length=30)),
                ('sendersTel', models.CharField(max_length=30)),
                ('recipientTel', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=30)),
                ('comment', models.TextField(max_length=300, null=True)),
                ('printNeed', models.BooleanField()),
            ],
        ),
    ]

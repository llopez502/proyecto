# Generated by Django 3.2.7 on 2021-10-01 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('centro_comercial', models.CharField(max_length=256)),
                ('direccion', models.CharField(max_length=256)),
            ],
        ),
    ]
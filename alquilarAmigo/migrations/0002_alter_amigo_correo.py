# Generated by Django 5.0.3 on 2024-04-07 01:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilarAmigo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='amigo',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]

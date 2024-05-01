# Generated by Django 5.0.3 on 2024-04-29 22:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilarAmigo', '0003_alter_user_name_user_alter_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='contrasena',
            field=models.CharField(default=0, max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='descripcion',
            field=models.TextField(default='null', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(blank=True, max_length=8),
        ),
        migrations.AddField(
            model_name='cliente',
            name='ubicacion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='alquilarAmigo.direccion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='correo',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
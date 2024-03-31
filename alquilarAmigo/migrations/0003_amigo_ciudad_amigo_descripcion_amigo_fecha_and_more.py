# Generated by Django 5.0.3 on 2024-03-31 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alquilarAmigo', '0002_tarifa_amigo_fotos'),
    ]

    operations = [
        migrations.AddField(
            model_name='amigo',
            name='ciudad',
            field=models.CharField(default='Bolivia', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='descripcion',
            field=models.TextField(default='Soy un buen amigo', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='fecha',
            field=models.DateField(default='2003-07-24'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='localidad',
            field=models.CharField(default='Quillacollo', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='pais',
            field=models.CharField(default='Bolivia', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='tarifa',
            field=models.IntegerField(default=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='amigo',
            name='telefono',
            field=models.CharField(default=12345678, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='amigo',
            name='disponibilidad',
            field=models.BooleanField(blank=True, default=True),
        ),
    ]

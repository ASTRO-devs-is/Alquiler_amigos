# Generated by Django 5.0.2 on 2024-04-03 20:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=500)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('correo', models.EmailField(max_length=254)),
                ('fecha_nacimiento', models.DateField()),
                ('genero', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pais', models.CharField(max_length=60)),
                ('ciudad', models.CharField(max_length=60)),
                ('localidad', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('funcion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interes', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_post', models.CharField(max_length=500)),
                ('fecha_post', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rol', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Tarifa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tarifa', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_archivo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_user', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=8)),
                ('activado', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.CharField(blank=True, max_length=8)),
                ('descripcion', models.TextField(max_length=500)),
                ('fecha_nacimiento', models.DateField()),
                ('correo', models.EmailField(max_length=254)),
                ('disponibilidad', models.BooleanField(blank=True, default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('genero', models.IntegerField()),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='alquilarAmigo.direccion')),
                ('id_tarifa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.tarifa')),
            ],
        ),
        migrations.CreateModel(
            name='DisponibilidadDias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dias', models.CharField(max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.amigo')),
            ],
        ),
        migrations.CreateModel(
            name='DisponibilidadHoras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horaInicio', models.TimeField()),
                ('horaFin', models.TimeField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.amigo')),
            ],
        ),
        migrations.CreateModel(
            name='Favorito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_agregado', models.DateField(auto_now_add=True)),
                ('id_amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.amigo')),
                ('id_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntaje', models.IntegerField()),
                ('fecha_calificacion', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.post')),
            ],
        ),
        migrations.CreateModel(
            name='Salida',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion_salida', models.TextField()),
                ('fecha_salida', models.DateField()),
                ('hora_inicio_salida', models.TimeField()),
                ('hora_fin_salida', models.TimeField()),
                ('cita_realizada', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('amigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.amigo')),
                ('categoria_salida', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.categoria')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_chat', models.DateField(auto_now_add=True)),
                ('activo_chat', models.BooleanField(default=True)),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.salida')),
            ],
        ),
        migrations.CreateModel(
            name='Archivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_archivo', models.CharField(max_length=255)),
                ('archivo', models.BinaryField()),
                ('fehca_archivo', models.DateField(auto_now_add=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.post')),
                ('tipo_archivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.tipo_archivo')),
            ],
        ),
        migrations.CreateModel(
            name='Reporte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reporte', models.CharField(max_length=500)),
                ('fecha_reporte', models.DateField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.user')),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.user'),
        ),
        migrations.CreateModel(
            name='Categoria_Interes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo_ci', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.categoria')),
                ('interes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.interes')),
            ],
            options={
                'unique_together': {('categoria', 'interes')},
            },
        ),
        migrations.CreateModel(
            name='ROl_Funcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo_rf', models.BooleanField(default=True)),
                ('funcion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.funcion')),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.rol')),
            ],
            options={
                'unique_together': {('rol', 'funcion')},
            },
        ),
        migrations.CreateModel(
            name='User_Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo_uc', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.categoria')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.user')),
            ],
            options={
                'unique_together': {('user', 'categoria')},
            },
        ),
        migrations.CreateModel(
            name='User_Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo_ui', models.BooleanField(default=True)),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.idioma')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.user')),
            ],
            options={
                'unique_together': {('user', 'idioma')},
            },
        ),
        migrations.CreateModel(
            name='User_Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activo_ur', models.BooleanField(default=True)),
                ('fecha_desde', models.DateField(auto_now_add=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.rol')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alquilarAmigo.user')),
            ],
            options={
                'unique_together': {('user', 'rol')},
            },
        ),
    ]

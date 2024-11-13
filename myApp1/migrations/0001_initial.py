# Generated by Django 5.1.2 on 2024-11-12 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EsActivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EstadoEstudiante', models.CharField(max_length=10)),
                ('FechaInsc', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facultad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facult', models.CharField(max_length=8)),
            ],
        ),
        migrations.CreateModel(
            name='postulado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=30)),
                ('Apellidos', models.CharField(max_length=30)),
                ('Cedula_P', models.CharField(max_length=8)),
                ('Fechanacimiento', models.DateField()),
                ('GrupoEtnico', models.CharField(max_length=30)),
                ('N_TLF', models.CharField(max_length=12)),
                ('Direccion', models.CharField(max_length=100)),
                ('CorreoE', models.CharField(max_length=30)),
                ('Fecha_postulacion', models.DateTimeField(auto_now_add=True)),
                ('estatus', models.TextField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ppostulador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=30)),
                ('Apellino', models.CharField(max_length=30)),
                ('CedulaPostulador', models.CharField(max_length=9)),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=20)),
                ('facultad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carreras', to='myApp1.facultad')),
            ],
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('par', models.CharField(max_length=10)),
                ('perioIns', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp1.esactivo')),
            ],
        ),
        migrations.AddField(
            model_name='esactivo',
            name='idinscrito',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp1.postulado'),
        ),
        migrations.CreateModel(
            name='postuladoDAcademicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ColegioEgreso', models.CharField(max_length=50)),
                ('AnoGraduacion', models.CharField(max_length=4)),
                ('Trabaja', models.CharField(max_length=4)),
                ('TrabajsComentario', models.CharField(max_length=100)),
                ('EstudiosPrevios', models.CharField(max_length=4)),
                ('ComentarioEstudios', models.CharField(max_length=100)),
                ('Programa', models.CharField(max_length=100)),
                ('Carrer_a_postular', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp1.carreras')),
                ('idPostulado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp1.postulado')),
                ('idDPostulador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp1.ppostulador')),
            ],
        ),
        migrations.CreateModel(
            name='requisi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PruebaObsu', models.CharField(max_length=11)),
                ('TituloBachiller', models.CharField(max_length=11)),
                ('fotoCopiaCedula', models.CharField(max_length=11)),
                ('NotasCertificadas', models.CharField(max_length=11)),
                ('fotos', models.CharField(max_length=11)),
                ('idpostulado', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='myApp1.postulado')),
            ],
        ),
    ]

# Generated by Django 4.2.2 on 2023-10-13 00:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inscripcionFinales', '0002_alter_usuario_sexo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Directivo',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('cargo', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('inscripcionFinales.usuario',),
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('matricula', models.CharField(max_length=10, unique=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('inscripcionFinales.usuario',),
        ),
        migrations.CreateModel(
            name='Preceptor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('area', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('inscripcionFinales.usuario',),
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('especialidad', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('inscripcionFinales.usuario',),
        ),
        migrations.CreateModel(
            name='usuarios_materias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='rol',
            field=models.CharField(choices=[('Directivo', 'Directivo'), ('Preceptor', 'Preceptor'), ('Profesor', 'Profesor'), ('Estudiante', 'Estudiante'), ('Administrador', 'Administrador')], default='Profesor', max_length=20),
        ),
        migrations.CreateModel(
            name='usuarios_materia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota_cursada', models.FloatField(blank=True, null=True, verbose_name='Nota de Cursada')),
                ('nota_final', models.FloatField(blank=True, null=True, verbose_name='Nota de Final')),
                ('aprobada', models.BooleanField(default=False)),
                ('modalidad', models.CharField(blank=True, choices=[('01', 'Regular'), ('02', 'Libre'), ('03', 'Condicional')], max_length=2, null=True, verbose_name='Modalidad')),
                ('ciclo_lectivo', models.CharField(blank=True, max_length=100, null=True, unique=True, verbose_name='Ciclo lectivo')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripcionFinales.materia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llamado', models.DateTimeField(verbose_name='Llamado')),
                ('vigente', models.BooleanField(default=True)),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripcionFinales.materia')),
            ],
        ),
        migrations.CreateModel(
            name='inscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aprobada', models.BooleanField(null=True)),
                ('llamado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripcionFinales.mesa')),
                ('materia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inscripcionFinales.materia')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

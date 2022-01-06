# Generated by Django 4.0 on 2021-12-29 22:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0003_curso_alumno_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='date_create',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alumno',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='birthday',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha de nacimiento'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='first_name',
            field=models.CharField(default='Coloque el nombre', max_length=30, verbose_name='Nombre'),
        ),
        migrations.AlterField(
            model_name='alumno',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Apellido'),
        ),
    ]
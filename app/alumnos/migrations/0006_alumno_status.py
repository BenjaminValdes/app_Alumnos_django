# Generated by Django 4.0 on 2021-12-29 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0005_curso_date_create_curso_last_update'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='status',
            field=models.CharField(choices=[('A', 'Activo'), ('B', 'Baja'), ('C', 'Cursando')], default='A', max_length=4, verbose_name='Estado'),
        ),
    ]
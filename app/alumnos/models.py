from django.db import models
from django.contrib.auth.models import User


class Curso(models.Model):
    name = models.CharField(max_length=30)
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['name']

    def save(self, *args, **kwargs):
        if self.id is None:
            self.name = f'C01-{self.name}'
        super(Curso, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.name.title()}'

class Alumno(models.Model):
    STATUS_CHOICES = (
        ('A', 'Activo'),
        ('B', 'Baja'),
        ('C', 'Cursando')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                            null=True, blank=True)
    first_name = models.CharField('Nombre', max_length=30, default='Coloque el nombre')
    last_name = models.CharField('Apellido',max_length=30)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE,
                              null=True, blank=True)
    status = models.CharField('Estado',max_length=4, choices=STATUS_CHOICES,
                              default='A')
    birthday = models.DateTimeField('Fecha de nacimiento', null=True, blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ['user']

    def __str__(self):
        return f'{self.last_name.title()}, {self.first_name.title()}'

    def save(self, *args, **kwargs):
        if self.id is None:
            Curso.objects.create(name = self.first_name)
        super(Alumno, self).save(*args, **kwargs)
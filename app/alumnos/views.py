from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
import datetime
from django.shortcuts import render

from .models import Alumno
from .forms import AlumnoForm


def get_alumnos(request):
    alumnos = Alumno.objects.all()
    form = AlumnoForm()
    error = False
    if request.method == "POST":
        form = AlumnoForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:    
            error = True
    return render(request, 'alumno_list.html',
                  context={'alumnos': alumnos,
                           'error': error,
                           'form': form})


@login_required
def alumno(request, id_alumno):
    alumno = Alumno.objects.get(pk=id_alumno)
    form = AlumnoForm(instance=alumno)
    if request.method == 'POST':
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save(commit=True)
    return render(request, 'alumno_detail.html',
                 context={'alumno': alumno,
                          'form': form})

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import datetime

from .models import Alumno
from .forms import CommentForm


def add_alumno(request):
    Alumno.objects.create(first_name=request.GET.get('name', '-'),
                          last_name=request.GET.get('lastname', '-'))
    response = {'status': 'OK'}
    return JsonResponse(response)


def get_alumnos(request):
    alumnos = Alumno.objects.all()
    form = CommentForm()
    return render(request, 'alumno_list.html', context={'alumnos': alumnos,
                                                        'title': "Alumnos: listado",
                                                        'now': datetime.datetime.now(),
                                                        'name': '<h1>Benjamin</h1>',
                                                        'form': form})



def alumno(request, id_alumno):
    alumno = Alumno.objects.get(pk=id_alumno)
    return render(request, 'alumno_detail.html', context={'alumno': alumno})
    


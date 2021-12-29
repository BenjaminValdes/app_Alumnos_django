from django.urls import path
from .views import get_alumnos, alumno

urlpatterns = [
    path('', get_alumnos),
    path('<int:id_alumno>', alumno)
]

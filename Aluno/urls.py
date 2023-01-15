from django.contrib import admin
from django.urls import path
from .views import  home_aluno,\
                    aluno_curso
 

urlpatterns = [

    path('aluno_home/',  home_aluno, name = 'sweet_home'),
    path('aluno_curso/<int:curso_id>', aluno_curso, name = 'curso_aluno')
    
]

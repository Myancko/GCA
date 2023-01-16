from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from .views import  home_aluno,\
                    aluno_curso,\
                    modal_selecionarAC,\
                    requisitar_aproveitamento_de_disciplina,\
                    requisitar_certificacao_de_conhecimento,\
                    modal_menu
 

urlpatterns = [

    path('aluno_home/',  home_aluno, name = 'sweet_home'),
    path('aluno_curso/<int:curso_id>', aluno_curso, name = 'curso_aluno'),
    
    path('requisitar_aproveitamento_de_disciplina',  requisitar_aproveitamento_de_disciplina, name='r_aproveitamento'),
    path('requisitar_certificacao_de_conhecimento',  requisitar_certificacao_de_conhecimento, name='r_certificacao'),
    
    path('teste/modais', modal_selecionarAC, name = 'modal'),
    path('teste/modal_menu', modal_menu, name = 'modal_menu'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

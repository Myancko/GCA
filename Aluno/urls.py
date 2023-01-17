from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from .views import  home_aluno,\
                    aluno_curso,\
                    modal_selecionarAC,\
                    modal_menu,\
                    requisitar_aproveitamento_de_disciplina_class,\
                        requisitar_certificacao_de_conhecimento,\
                    requisitar_certificacao_de_conhecimento_class

"""requisitar_aproveitamento_de_disciplina
requisitar_certificacao_de_conhecimento""" 

urlpatterns = [


    path('aluno_home/',  home_aluno, name = 'sweet_home'),
    path('aluno_curso/<int:curso_id>', aluno_curso, name = 'curso_aluno'),
    
    path('requisitar_aproveitamento_de_disciplina/<int:disciplina_id>', requisitar_aproveitamento_de_disciplina_class.as_view(), name='r_aproveitamento'),
    #path('requisitar_aproveitamento_de_disciplina/<int:disciplina_id>',  requisitar_aproveitamento_de_disciplina, name='r_aproveitamento'),
    #path('requisitar_certificacao_de_conhecimento/<int:disciplina_id>',  requisitar_certificacao_de_conhecimento, name='r_certificacao'),
    path('requisitar_certificacao_de_conhecimento/<int:disciplina_id>',  requisitar_certificacao_de_conhecimento_class.as_view(), name='r_certificacao'),
    path('teste/modais', modal_selecionarAC, name = 'modal'),
    path('teste/modal_menu', modal_menu, name = 'modal_menu'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

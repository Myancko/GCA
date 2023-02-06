from django.conf.urls.static import static
from django.conf import settings

from django.contrib import admin
from django.urls import path
from .views import  home_aluno,\
                    aluno_curso,\
                    vizualizar_minhas_requisicoes_de_aproveitamento,\
                    vizualizar_minhas_requisicoes_de_certificacao,\
                    password_change,\
                    requisitar_aproveitamento_de_disciplina,\
                    requisitar_certificacao_de_conhecimento_class
                        


"""requisitar_aproveitamento_de_disciplina
requisitar_certificacao_de_conhecimento""" 

urlpatterns = [


    path('aluno_home/',  home_aluno, name = 'sweet_home'),
    path('aluno_home/alterar_senha/',  password_change.as_view(), name = 'student_change_password'),
    path('aluno_curso/<int:curso_id>', aluno_curso, name = 'curso_aluno'),
    
    #path('requisitar_aproveitamento_de_disciplina/<int:disciplina_id>', requisitar_aproveitamento_de_disciplina_class.as_view(), name='r_aproveitamento'),
    path('requisitar_aproveitamento_de_disciplina/<int:disciplina_id>',  requisitar_aproveitamento_de_disciplina, name='r_aproveitamento'),
    #path('requisitar_certificacao_de_conhecimento/<int:disciplina_id>',  requisitar_certificacao_de_conhecimento, name='r_certificacao'),
    path('requisitar_certificacao_de_conhecimento/<int:disciplina_id>',  requisitar_certificacao_de_conhecimento_class.as_view(), name='r_certificacao'),
    
    path('aluno_requisicoes/aproveitamento/', vizualizar_minhas_requisicoes_de_aproveitamento, name='aluno_requisicoes_de_aproveitamento'),
    path('aluno_requisicoes/certificacao/', vizualizar_minhas_requisicoes_de_certificacao, name='aluno_requisicoes_de_certificacao')
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

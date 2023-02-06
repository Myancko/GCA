from django.urls import path
from Aluno.views import password_change
from .views import  home_professor,\
                    lista_aproveitamento,\
                    lista_certificacao_professor,\
                    lista_certificacao,\
                    aproveitamento,\
                    certificacao,\
                    iniciar_periodo_disciplina,\
                    iniciar_periodo_de_certificacao_listagem_disciplinas,\
                    search_aproveitamento,\
                    search_certificacao
urlpatterns = [
    
    path('home_coordenador/', home_professor, name='sweet-home_teacher'),
    path('lista_disciplinas_iniciar_certificacao/<int:curso_id>', iniciar_periodo_de_certificacao_listagem_disciplinas, name='iniciar_certificacao'),
    path('Iniciar_periodo_de_requisicao/<int:disciplina_id>', iniciar_periodo_disciplina, name='iniciar_periodo'),
    path('lista_aproveitamento/', lista_aproveitamento, name='aproveitamento_list'),
    path('lista_certificacao/professor/<int:id>', lista_certificacao_professor, name='certificacao_list_professor'),
    path('lista_certificacao/', lista_certificacao, name='certificacao_list'),
    path('lista_aproveitamento/<int:aproveitamento_id>', aproveitamento, name='aproveitamento'),
    path('lista_certificacao/<int:certificacao_id>', certificacao, name='certificacao'),
    path('professor_home/alterar_senha/',  password_change.as_view(), name = 'teacher_change_password'),

    path('lista_aproveitamento/ajax/<str:text>', search_aproveitamento, name = 'ajax-aproveitamento'),
    path('lista_certificacao/ajax/<str:text>', search_certificacao, name = 'ajax-certificacao'),
]
from django.urls import path
from Aluno.views import password_change
from .views import  home_professor,\
                    lista_aproveitamento,\
                    lista_certificacao,\
                    aproveitamento,\
                    certificacao
urlpatterns = [
    
    path('home_coordenador/', home_professor, name='sweet-home_teacher'),
    path('lista_aproveitamento/', lista_aproveitamento, name='aproveitamento_list'),
    path('lista_certificacao/', lista_certificacao, name='certificacao_list'),
    path('lista_aproveitamento/<int:aproveitamento_id>', aproveitamento, name='aproveitamento'),
    path('lista_certificacao/<int:certificacao_id>', certificacao, name='certificacao'),
    path('professor_home/alterar_senha/',  password_change.as_view(), name = 'teacher_change_password'),
]
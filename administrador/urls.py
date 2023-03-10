from django.contrib import admin
from django.urls import path
from .views import  home_view,\
                    sign_up_course_view,\
                    sign_up_subject_view,\
                    register_coordinator_view,\
                    teste_view,\
                    SignUpView_Student,\
                    SignUpView_Teacher,\
                    lista_cursos,\
                    lista_Disciplinas,\
                    lista_Aluno,\
                    lista_Professors,\
                    diciplina_especifica,\
                    aluno_especifico,\
                    professor_especifico,\
                    curso_especifico,\
                    search_aluno,\
                    search_professor,\
                    search_curso,\
                    search_disciplina,\
                    CONFIG

urlpatterns = [

    path('',  home_view, name = 'home'),

    path('adm/sigh_up_student/cadastro_Estudante/', SignUpView_Student.as_view(), name='cadastro_estudante'),
    path('adm/sigh_up_student/cadastro_Professor/', SignUpView_Teacher.as_view(), name='cadastro_professor'),

    path('adm/sigh_up_course',  sign_up_course_view, name = 'sign_up_course'),
    path('adm/sigh_up_subject',  sign_up_subject_view, name = 'sign_up_subject'),
    path('adm/register_coordinator',  register_coordinator_view, name = 'register_coordinator'),
    
    path('adm/list_courses/',  lista_cursos, name = 'lista_cursos'),
    path('adm/list_subjects/',  lista_Disciplinas, name = 'lista_disciplinas'),
    path('adm/list_students/',  lista_Aluno, name = 'lista_Aluno'),
    path('adm/list_coordinator/',  lista_Professors, name = 'lista_professor'),
    
    path('adm/disciplina/<int:id>', diciplina_especifica, name = 'disciplina'),
    path('adm/aluno/<int:id>', aluno_especifico, name = 'aluno'),
    path('adm/professor/<int:id>', professor_especifico, name = 'professor'),
    path('adm/curso/<int:id>', curso_especifico, name = 'curso'),
    path('adm/professor/<int:id>', professor_especifico, name = 'professor'),
    
    path('adm/list_students_ajax/<str:text>', search_aluno, name='ajax_lista_aluno' ),
    path('adm/list_teacher_ajax/<str:text>', search_professor, name='ajax_lista_professor' ),
    path('adm/list_course_ajax/<str:text>', search_curso, name='ajax_lista_curso' ),
    path('adm/list_subject_ajax/<str:text>', search_disciplina, name='ajax_lista_disciplina' ),
    
    path('CONFIG/<int:id>', CONFIG, name = 'CONFIG'),
    path('adm/teste',  teste_view, name = 'teste'),
]

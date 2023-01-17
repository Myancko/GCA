from tokenize import group
from django.http import Http404
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Disciplina, Curso 
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group
from django.db.models import Q
from django.shortcuts import redirect

from .form import Form_disciplina, Form_Curso
from Users import forms
from .models import Disciplina, Curso

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

"""
>>> from Users.models import CustomUser
>>> user = CustomUser.objects.get(id=28)
>>> user
<CustomUser: 2312321>
>>> user.groups
<django.db.models.fields.related_descriptors.create_forward_many_to_many_manager.<locals>.ManyRelatedManager object at 0x00000227AD051120>
>>> user.groups.all()
<QuerySet [<Group: Professor>]>
>>> from django.contrib.auth.models import Group
>>> group = Group.objects.get(name="Professor") 
>>> user.groups.contains(group)
True
>>> 
"""


@login_required(login_url='/user/login/')
def home_view (request):

    logged = request.user
    
   
    teacher_group = Group.objects.get(name='Professor')
    student_group = Group.objects.get(name='Aluno')
    
    try:
        if logged.groups.get() == "Professor":
            print("e professor!!!")
        if logged.groups.get()  == "Aluno":
            print("e Aluno")
    except: 
        print('sei oq é n, provavelmente adinistrador :/')
    

    if logged.is_superuser == True:
        print('e adminitrador') 
        
    elif logged.groups.get() == student_group:
        print('pq?<<<<<<<<<<<<<<<<<<<<')
        aluno = redirect ('Aluno/aluno_home/', {})
        return aluno

    elif logged.groups.get() == teacher_group:
        print('pq?<<<<<<<<<<<<<<<<<<<<')
        aluno = redirect ('Coordenador/home_coordenador/', {})
        return aluno

    print(logged.groups)
    
    
    curso_list =  Curso.objects.all()
    disciplina_total =  len(Disciplina.objects.all())
    
    total_de_professores = len(User.objects.filter(groups=teacher_group))
    total_de_alunos = len(User.objects.filter(groups=student_group))
    
    
    context = {
        "teacher": total_de_professores,
        "student": total_de_alunos,
        'course': len(curso_list),
        "disciplina" :  disciplina_total
    }


    return render(request, 'home.html',  context)

class SignUpView_Student(CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up_student.html'
    model = CustomUser

    def form_valid(self, form):
        response = super().form_valid(form)

        student_group = Group.objects.get(name='Aluno')
        self.object.groups.add(student_group)

        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response

class SignUpView_Teacher(CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up_teacher.html'
    model = CustomUser

    def form_valid(self, form):
        response = super().form_valid(form)
        form.save_m2m()
        
        teacher_group = Group.objects.get(name='Professor')
        self.object.groups.add(teacher_group)

        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response

def sign_up_course_view (request):

    form = Form_Curso()
    if request.method == "POST":
        form = Form_Curso(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'sign_up_course.html', context)
    
    else:
        form = Form_Curso()
        context = {   
            'form':form
        }
        return render(request, 'sign_up_course.html', context)

    return render(request, 'sign_up_course.html',  {})

def sign_up_subject_view (request):

    form = Form_disciplina()
    if request.method == "POST":
        form = Form_disciplina(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'sign_up_disciplina.html', context)
    
    else:
        form = Form_disciplina()
        context = {   
            'form':form
        }
        return render(request, 'sign_up_disciplina.html', context)

    return render(request, 'sign_up_disciplina.html',  {})

def register_coordinator_view (request):

    return render(request, 'register.coordinator.html',  {})

def teste_view (request):
    disciplina = Disciplina.objects.all()
    curso = Curso.objects.all()

    context = {
        'disciplina' : disciplina,
        'curso' : curso,
    }
    return render(request, 'teste.html',  context)

         
def lista_cursos(request):
    
    lista_de_cursos = Curso.objects.all()
    len_cursos = len(Curso.objects.all())

    return render(request, 'curso_list.html', {'curso' : lista_de_cursos,
                                               'len': len_cursos})

def lista_Disciplinas(request):
    
    lista_de_disciplinas = Disciplina.objects.all()
    len_disciplinas = len(Disciplina.objects.all())
    

    return render(request, 'disciplina_lista.html', {'disciplina' : lista_de_disciplinas,
                                                     'len': len_disciplinas})
    
def lista_Aluno(request):
    
    student_group = Group.objects.get(name='Aluno')
    student = User.objects.all().filter(groups=student_group)
    total_de_alunos = len(User.objects.filter(groups=student_group))
    
    
    #otal_de_alunos_cadastrados_em_disciplinas = User.objects.filter(Q(groups=student_group)) #E´possivel filtrar grupos e curso
    

    return render(request, 'aluno_lista.html', {'grupo_aluno': total_de_alunos,
                                                "aluno": student})
    
def lista_Professors(request):
    
    teacher_group = Group.objects.get(name='Professor')
    teacher = User.objects.all().filter(groups=teacher_group)

    total_de_professores = len(User.objects.filter(groups=teacher_group))
    
    
    #otal_de_alunos_cadastrados_em_disciplinas = User.objects.filter(Q(groups=student_group)) #E´possivel filtrar grupos e curso
    

    return render(request, 'professor_lista.html', {'grupo_professor': total_de_professores,
                                                "professor": teacher})
    

def diciplina_especifica (request, id):
    
    disciplina = Disciplina.objects.all()
    disciplina  = Disciplina.objects.get(id=id)
    m2m  = disciplina.dependencia.all()
    
    return render (request, 'subject.html', {'disciplina': disciplina,
                                             'disciplina_dependencias':m2m})
from email.headerregistry import Group
from tokenize import group
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Disciplina, Curso 

from django.views.generic.edit import CreateView
#create
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from Users.models import CustomUser
from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth.models import Group

from Users import forms

from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

@login_required(login_url='/user/login/')
def home_view (request):

    teacher_group = Group.objects.get(name='Professor')
    student_group = Group.objects.get(name='Aluno')

    total_de_professores = len(User.objects.filter(groups=teacher_group))
    total_de_alunos = len(User.objects.filter(groups=student_group))
    
    context = {
        "teacher": total_de_professores,
        "student": total_de_alunos
    }


    return render(request, 'home.html',  context)

class SignUpView_Student(CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('login')
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
    success_url = reverse_lazy('login')
    template_name = 'sign_up_teacher.html'
    model = CustomUser

    def form_valid(self, form):
        response = super().form_valid(form)

        teacher_group = Group.objects.get(name='Professor')
        self.object.groups.add(teacher_group)

        messages.success(self.request, "Usuário cadastrado com sucesso!")
        return response



def sign_up_student_view (request):

    

    return render(request, 'sign_up_student.html',  {})

def sign_up_teacher_view (request):

    return render(request, 'sign_up_teacher.html',  {})


def sign_up_course_view (request):

    return render(request, 'sign_up_course.html',  {})

def sign_up_subject_view (request):

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



def cadastro(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
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
from django.contrib.auth.mixins import LoginRequiredMixin

from .form import Form_disciplina, Form_Curso
from Users import forms
from .models import Disciplina, Curso
from Aluno.models import Certificação_de_conhecimento
from django.http import JsonResponse
from datetime import date

from Users.forms import CustomUserCreateForm,  CustomUserChangeForm, CustomUserChangeForm_Config
import random
from django.core.mail import send_mail

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
    
    expirar_disciplinas = Disciplina.objects.all()
    for disciplina in expirar_disciplinas:
        print(disciplina.data_final, '<<<<<<<')   
        if disciplina.data_final != None:
            if disciplina.data_final > date.today():
                print(disciplina.nome,'expirou')
                disiciplina_q_expirou = disciplina
                disiciplina_q_expirou.banca_de_professores.clear()
                disiciplina_q_expirou.pedagogo = None
                disiciplina_q_expirou.aberto = False
                disiciplina_q_expirou.data_final = None
                disciplina.save()
                try:
                    certificacao = Certificação_de_conhecimento.objects.get(disciplina=disciplina.id)
                    print(certificacao, disciplina, certificacao.nota,'<<<') 

                    if certificacao.nota >= 60:
                          print('aluno', certificacao.requisitor.username, 'aprovado')
                          certificacao.status_requisição = 'aprovado'
                          aluno_aprovado = User.objects.get(id=certificacao.requisitor.id)
                          print(aluno_aprovado,'<<<')
                          aluno_aprovado.disciplina_concluidas.add(disciplina)
                          print(aluno_aprovado.disciplina_concluidas.all(),  '<<< ')                     
                          certificacao.save()
                          aluno_aprovado.save()
                    elif certificacao.nota < 60:
                          print('aluno', certificacao.requisitor.username, 'reprovado')
                          certificacao.status_requisição = 'reprovado'
                          certificacao.save()
                except:
                    messages.warning(request, 'Não Existem requisições pra a certificacao de conhecimento da disciplina' + str( disciplina.nome ))
                    return redirect('home')  
            else:
                print(disciplina.nome, disciplina.data_final,'ainda n expirou')
        else:
            print('disciplina sem data para certificacao de conhecimento.')

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


class SignUpView_Student(LoginRequiredMixin,CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up_student.html'
    login_url = '/user/login/'
    model = CustomUser
    
    def get(self, request, *args, **kwargs):
        
        if request.user.is_superuser == True:
            print('e adminitrador') 

            x = random.randint(0,100000)
            y = random.randint(0,100000)
            z = ''
            v = 'abcdefghijklmnopqrstuvwxyz'
            cont = 0
            total_letras =  random.randint(5,15)
            loop = total_letras
            while cont <= total_letras:
                loop = random.randint(0,25)
                z += v[loop]
                cont += 1

            senha_temporaria = z + str(x) + str(y) + '.'

            self.extra_context= {'senha': senha_temporaria}
            return super().get(request, *args, **kwargs)
        
        else:
            
            return redirect ('http://127.0.0.1:8000/',{})
    
    def post(self, request, *args, **kwargs):
        
        if request.user.is_superuser == True:
            print('e adminitrador') 

            x = random.randint(0,100000)
            y = random.randint(0,100000)
            z = ''
            v = 'abcdefghijklmnopqrstuvwxyz'
            cont = 0
            total_letras =  random.randint(5,15)
            loop = total_letras
            while cont <= total_letras:
                loop = random.randint(0,25)
                z += v[loop]
                cont += 1

            senha_temporaria = z + str(x) + str(y) + '.'

            self.extra_context= {'senha': senha_temporaria}
            return super().post(request, *args, **kwargs)
        
        else:
            
            return redirect ('http://127.0.0.1:8000/',{})
    

    def form_valid(self, form):
        
        print(form)
        response = super().form_valid(form)

        student_group = Group.objects.get(name='Aluno')
        self.object.groups.add(student_group)

        matricula = form.cleaned_data['matricula']
        username = form.cleaned_data['username']
        senha = form.cleaned_data['password2']
        email = form.cleaned_data['email']
        msg = 'Ola Aluno '+ str(username) + '\nSua matricula é: ' +  str(matricula)+'\nSua senha é: '+str(senha)
        
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        
        return response
    
    def form_invalid(self, form):
        
        return super().form_invalid(form)
    

class SignUpView_Teacher(LoginRequiredMixin,CreateView):
    form_class = forms.CustomUserCreateForm
    success_url = reverse_lazy('home')
    template_name = 'sign_up_teacher.html'
    login_url = '/user/login/'
    model = CustomUser
    
    def get(self, request, *args, **kwargs):
        
        if request.user.is_superuser == True:
            x = random.randint(0,100000)
            y = random.randint(0,100000)
            z = ''
            v = 'abcdefghijklmnopqrstuvwxyz'
            cont = 0
            total_letras =  random.randint(5,15)
            loop = total_letras
            while cont <= total_letras:
                loop = random.randint(0,25)
                z += v[loop]
                cont += 1

            senha_temporaria = z + str(x) + str(y) + '.'

            self.extra_context= {'senha': senha_temporaria}
            return super().get(request, *args, **kwargs)
        
        else:
            
            return redirect ('http://127.0.0.1:8000/',{})
    
    def post(self, request, *args, **kwargs):
        
        if request.user.is_superuser == True:
            x = random.randint(0,100000)
            y = random.randint(0,100000)
            z = ''
            v = 'abcdefghijklmnopqrstuvwxyz'
            cont = 0
            total_letras =  random.randint(5,15)
            loop = total_letras
            while cont <= total_letras:
                loop = random.randint(0,25)
                z += v[loop]
                cont += 1

            senha_temporaria = z + str(x) + str(y) + '.'

            self.extra_context= {'senha': senha_temporaria}
            return super().post(request, *args, **kwargs)
        
        else:
            
            return redirect ('http://127.0.0.1:8000/',{})

    def form_valid(self, form):
        
        print(form)
        response = super().form_valid(form)
        form.save_m2m()

        teacher_group = Group.objects.get(name='Professor')
        self.object.groups.add(teacher_group)

        matricula = form.cleaned_data['matricula']
        username = form.cleaned_data['username']
        senha = form.cleaned_data['password2']
        email = form.cleaned_data['email']
        msg = 'Ola Professor '+ str(username) + '\nSua matricula é: ' +  str(matricula)+'\nSua senha é: '+str(senha)
        res = send_mail( 'Login e Senha do GCA',msg,'projectgca394@gmail.com',['weptpear394@gmail.com'])
        messages.success(self.request, "Usuário cadastrado com sucesso!")
        
        return response
    
    def form_invalid(self, form):
        
        return super().form_invalid(form)

@login_required(login_url='/user/login/')
def sign_up_course_view (request):

    if request.user.is_superuser == True:
        form = Form_Curso()
        teacher_group = Group.objects.get(name='Professor')   
        professores = User.objects.filter(groups=teacher_group)

        if request.method == "POST":
            form = Form_Curso(request.POST)
            if form.is_valid():
                coordenador = form.cleaned_data['coordenador']

                form.save()

                curso = Curso.objects.latest('id')
                prof = User.objects.filter(id=coordenador.id).update(curso_relacao=curso.id)
                try:
                    for objects in prof:
                        objects.save()
                except:
                    return HttpResponseRedirect(reverse('home'))
            else:
                context = {   
                'form':form,
                'prof':professores
                }
                return render(request, 'sign_up_course.html', context)

        else:
            form = Form_Curso()
            context = {   
                'form':form,
                'prof':professores
            }
            return render(request, 'sign_up_course.html', context)
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})
    
    return render(request, 'sign_up_course.html',  {})

@login_required(login_url='/user/login/')
def sign_up_subject_view (request):

    if request.user.is_superuser == True:
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
    
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def register_coordinator_view (request):
    if request.user.is_superuser == True:
        return render(request, 'register.coordinator.html',  {})
    else:
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def teste_view (request):
    
    if request.user.is_superuser == True:
        disciplina = Disciplina.objects.all()
        curso = Curso.objects.all()

        context = {
            'disciplina' : disciplina,
            'curso' : curso,
        }
        return render(request, 'teste.html',  context)
    
    else:
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')         
def lista_cursos(request):
    
    if request.user.is_superuser == True:
        lista_de_cursos = Curso.objects.all()
        len_cursos = len(Curso.objects.all())

        return render(request, 'curso_list.html', {'curso' : lista_de_cursos,
                                                   'len': len_cursos})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def lista_Disciplinas(request):
    
    if request.user.is_superuser == True:
        lista_de_disciplinas = Disciplina.objects.all()
        len_disciplinas = len(Disciplina.objects.all())


        return render(request, 'disciplina_lista.html', {'disciplina' : lista_de_disciplinas,
                                                         'len': len_disciplinas})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def lista_Aluno(request):
    
    if request.user.is_superuser == True:
        student_group = Group.objects.get(name='Aluno')
        student = User.objects.all().filter(groups=student_group)
        total_de_alunos = len(User.objects.filter(groups=student_group))


        #otal_de_alunos_cadastrados_em_disciplinas = User.objects.filter(Q(groups=student_group)) #E´possivel filtrar grupos e curso


        return render(request, 'aluno_lista.html', {'grupo_aluno': total_de_alunos,
                                                    "aluno": student})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def lista_Professors(request):
    
    if request.user.is_superuser == True:
        teacher_group = Group.objects.get(name='Professor')
        teacher = User.objects.all().filter(groups=teacher_group)

        total_de_professores = len(User.objects.filter(groups=teacher_group))


        #otal_de_alunos_cadastrados_em_disciplinas = User.objects.filter(Q(groups=student_group)) #E´possivel filtrar grupos e curso


        return render(request, 'professor_lista.html', {'grupo_professor': total_de_professores,
                                                    "professor": teacher})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})
    
@login_required(login_url='/user/login/')
def diciplina_especifica (request, id):
    
    if request.user.is_superuser == True:
        disciplina = Disciplina.objects.get(id=id)
        teacher_group = Group.objects.get(name='Professor')

        professores = User.objects.filter(groups=teacher_group)
        print(professores, '<<<')
        form = Form_disciplina(request.POST or None, request.FILES or None, instance = disciplina)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_cursos'))

        return render (request, 'subject.html', {'form':form,
                                                'disciplina':disciplina})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/') 
def aluno_especifico (request, id):
    
    if request.user.is_superuser == True:
        aluno = User.objects.get(id=id)

        print(type(aluno.image),' <<<<<<<<<<<<<<<<<')
    

        form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance = aluno)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_Aluno'))

        return render (request, 'student.html', {'form':form,
                                                 'aluno':aluno})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def professor_especifico (request, id):
    
    if request.user.is_superuser == True:
        professor = User.objects.get(id=id)

        print(type(professor.image),' <<<<<<<<<<<<<<<<<')
    

        form = CustomUserChangeForm(request.POST or None, request.FILES or None, instance = professor)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_professor'))

        return render (request, 'teacher.html', {'form':form,
                                                 'aluno':professor})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})
    
@login_required(login_url='/user/login/')
def curso_especifico (request, id):
    
    if request.user.is_superuser == True:
        curso = Curso.objects.get(id=id)
        teacher_group = Group.objects.get(name='Professor')

        professores = User.objects.filter(groups=teacher_group)
        print(professores, '<<<')
        form = Form_Curso(request.POST or None, request.FILES or None, instance = curso)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('lista_cursos'))

        return render (request, 'course.html', {'form':form,
                                                'curso':curso,
                                                'grupo_professor':professores})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})
    
@login_required(login_url='/user/login/')
def search_aluno(request, text):

    if request.user.is_superuser == True:
        group_aluno = Group.objects.get(name='Aluno')
        aluno = User.objects.filter(username__contains=text, groups=group_aluno)
        print(aluno)

        return render(request, 'ajax/ajax_aluno.html', {'aluno': aluno})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def search_professor(request, text):

    if request.user.is_superuser == True:
        group_prof = Group.objects.get(name='Professor')
        professor = User.objects.filter(username__contains=text, groups=group_prof)
        print(professor)

        return render(request, 'ajax/ajax_professor.html', {'professor': professor})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def search_curso(request, text):

    if request.user.is_superuser == True:
        curso = Curso.objects.filter(nome__contains=text)
        print(curso)

        return render(request, 'ajax/ajax_curso.html', {'curso': curso})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')
def search_disciplina(request, text):

    if request.user.is_superuser == True:
        disciplina = Disciplina.objects.filter(nome__contains=text)
        print(disciplina)

        return render(request, 'ajax/ajax_disciplina.html', {'disciplina': disciplina})
    else:
        
        return redirect ('http://127.0.0.1:8000/',{})

@login_required(login_url='/user/login/')  
def CONFIG (request, id):
    
    usuario = User.objects.get(id=id)
    
    group_prof = Group.objects.get(name='Professor')
    grupo_aluno = Group.objects.get(name='Aluno')
    
    print(type(usuario.image),' <<<<<<<<<<<<<<<<<')
   
    
    form = CustomUserChangeForm_Config(request.POST or None, request.FILES or None, instance = usuario)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))
    #   print(request.user.groups.all(), '<<<<<<<<<')
    for grupo in request.user.groups.all():
        user_grupo  =  str(grupo)
        print(user_grupo, type(user_grupo))
    return render (request, 'CONFIG.html', {'form':form,
                                            'aluno':usuario,
                                            'grupo':user_grupo})

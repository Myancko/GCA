from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse, reverse_lazy
from Users.forms import CustomUserCreateForm,  CustomUserChangeForm,  PasswordChangeForm
from django.shortcuts import render
from django.urls import reverse
from administrador.models import Curso, Disciplina
from Aluno.models import Aproveitamento_de_disciplina, Certificação_de_conhecimento
from django.contrib.auth import get_user_model
from Aluno.form import Form_aproveitamento_de_disciplina, Form_certificação_de_conhecimento
from django.db.models import Q
from django.shortcuts import redirect
from datetime import date
from .form import Form_disciplina_iniciar_perido_de_certificacao



User = get_user_model()

# Create your views here.

def home_professor (request):
    
    try:
        
        if request.user.primeiro_login == True:
        
            primeiro_login = redirect ('/Coordenador/professor_home/alterar_senha/', {})
            return primeiro_login
        
        coordenador = True
        professor = User.objects.get(id=request.user.id)
        professor_curso_name = professor.curso_relacao
        professor_curso_disciplinas = professor.curso_relacao.disciplina.all()
        requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.all()
        requisicoes_de_certificacao = Certificação_de_conhecimento.objects.all()

        print('coordenador de', professor_curso_name)
        lista_de_disciplinas_curso = set()
        aluno = []
        aluno_do_curso = set()
        aluno_do_disciplina = set()

        for dados in requisicoes_de_aproveitamento:
            print(dados, dados.disciplina.id,  dados.requisitor, '<<')
            if professor_curso_name == dados.requisitor.curso_relacao:
                print(dados, dados.disciplina.id,  dados.requisitor,  dados.requisitor.disciplina_relacao, '<<' 'acho')
                aluno_do_curso.add(dados.requisitor)

        for disciplnas in professor_curso_disciplinas.all():
            print(disciplnas, disciplnas.id, '<')
            lista_de_disciplinas_curso.add(disciplnas.id)


        for dados in aluno_do_curso:
            print(dados, ',,,,,')

        requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.filter (Q(requisitor__in = aluno_do_curso))
        
        requisicoes_de_certificacao = Certificação_de_conhecimento.objects.all()

        print('coordenador de', professor_curso_name)
        lista_de_disciplinas_curso = set()
        aluno = []
        aluno_do_curso = set()
        aluno_do_disciplina = set()

        for dados in requisicoes_de_certificacao:
            print(dados, dados.disciplina.id,  dados.requisitor, '<<')
            if professor_curso_name == dados.requisitor.curso_relacao:
                print(dados, dados.disciplina.id,  dados.requisitor,  dados.requisitor.disciplina_relacao, '<<' 'acho')
                aluno_do_curso.add(dados.requisitor)

        for disciplnas in professor_curso_disciplinas.all():
            print(disciplnas, disciplnas.id, '<')
            lista_de_disciplinas_curso.add(disciplnas.id)


        for dados in aluno_do_curso:
            print(dados, ',,,,,')

        requisicoes_de_certificacao = Certificação_de_conhecimento.objects.filter (Q(requisitor__in = aluno_do_curso))

        usuario = request.user
        print(usuario.curso_relacao.id)

        return render(request, 'home_professor.html', { 'total_aproveitamentos': len(requisicoes_de_aproveitamento),
                                                        'aproveitamento': requisicoes_de_aproveitamento,
                                                        'total_certificacao' : len (requisicoes_de_certificacao),
                                                        'certificacao' : requisicoes_de_certificacao,
                                                        'coordenador': coordenador,
                                                        'usuario':usuario})
    except:
        coordenador = False
        msg = 'Você não é Coordenador :p'
        return render(request, 'home_professor.html', {'coordenador': coordenador,
                                                       'msg': msg}) 
    
def iniciar_periodo_de_certificacao_listagem_disciplinas(request, curso_id):

    aluno = request.user

    #curso = Curso.objects.all()
    curso  = Curso.objects.get(id=curso_id)
    m2m  = curso.disciplina.all()
    len_disciplinas = len(curso.disciplina.all())
    
    len_optativas = 0
    len_nao_opttivas = 0
    
    for disciplina in m2m:
        if disciplina.optativa == 'S':
            len_optativas  +=1
        else:
            len_nao_opttivas += 1
    
    return  render (request, 'periodo_de_certificacao_listagem.html', {'curso': curso,
                                                       'disciplinas' : m2m,
                                                       'total_disciplinas' : len_disciplinas,
                                                       'total_de_optativas': len_optativas,
                                                       'total_de_nao_optativas' : len_nao_opttivas})
    
    return  render(request, 'periodo_de_certificacao_listagem.html', {})

def lista_aproveitamento (request):
    
    professor = User.objects.get(id=request.user.id)
    professor_curso_name = professor.curso_relacao
    professor_curso_disciplinas = professor.curso_relacao.disciplina.all()
    requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.all()
    
    print('coordenador de', professor_curso_name)
    lista_de_disciplinas_curso = set()
    aluno = []
    aluno_do_curso = set()
    aluno_do_disciplina = set()
    
    for dados in requisicoes_de_aproveitamento:
        print(dados, dados.disciplina.id,  dados.requisitor, '<<')
        if professor_curso_name == dados.requisitor.curso_relacao:
            print(dados, dados.disciplina.id,  dados.requisitor,  dados.requisitor.disciplina_relacao, '<<' 'acho')
            aluno_do_curso.add(dados.requisitor)
            
    for disciplnas in professor_curso_disciplinas.all():
        print(disciplnas, disciplnas.id, '<')
        lista_de_disciplinas_curso.add(disciplnas.id)
        
        
    for dados in aluno_do_curso:
        print(dados, ',,,,,')
    
    requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.filter (Q(requisitor__in = aluno_do_curso))
    
    return  render(request, 'requisicoes_aproveitamento_lista.html', {'aproveitamento': requisicoes_de_aproveitamento})

def lista_certificacao (request):
    
    professor = User.objects.get(id=request.user.id)
    professor_curso_name = professor.curso_relacao
    professor_curso_disciplinas = professor.curso_relacao.disciplina.all()
    requisicoes_de_certificacao = Certificação_de_conhecimento.objects.all()
    
    print('coordenador de', professor_curso_name)
    lista_de_disciplinas_curso = set()
    aluno = []
    aluno_do_curso = set()
    aluno_do_disciplina = set()
    
    for dados in requisicoes_de_certificacao:
        print(dados, dados.disciplina.id,  dados.requisitor, '<<')
        if professor_curso_name == dados.requisitor.curso_relacao:
            print(dados, dados.disciplina.id,  dados.requisitor,  dados.requisitor.disciplina_relacao, '<<' 'acho')
            aluno_do_curso.add(dados.requisitor)
            
    for disciplnas in professor_curso_disciplinas.all():
        print(disciplnas, disciplnas.id, '<')
        lista_de_disciplinas_curso.add(disciplnas.id)
        
        
    for dados in aluno_do_curso:
        print(dados, ',,,,,')
    
    requisicoes_de_certificacao = Certificação_de_conhecimento.objects.filter (Q(requisitor__in = aluno_do_curso))
    
    return  render(request, 'requisicoes_certificação_lista.html', {'certificacao': requisicoes_de_certificacao})

def iniciar_periodo_disciplina(request, disciplina_id):

    dados_disciplina = Disciplina.objects.get(id=disciplina_id)
    print(dados_disciplina)
    dependencias_disciplina = dados_disciplina.dependencia
    print(dependencias_disciplina)
    form = Form_disciplina_iniciar_perido_de_certificacao(request.POST or None, request.FILES or None, instance = dados_disciplina)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('home'))
    
    return render(request, 'iniciar_periodo_disciplina.html', {'disciplina':dados_disciplina,
                                                               'dependencias':dependencias_disciplina,
                                                               'form':form}) 


def aproveitamento (request, aproveitamento_id):
    
    aproveitamento = Aproveitamento_de_disciplina.objects.get(id=aproveitamento_id)
    
    form = Form_aproveitamento_de_disciplina(request.POST or None, instance = aproveitamento)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('aproveitamento_list'))
    
    requisitor = aproveitamento.requisitor
    
    print(requisitor)
    return render(request, 'aproveitamento.html' , {'aproveitamento': aproveitamento,
                                                    'form' : form})
    
def certificacao (request, certificacao_id):
    
    certificacao = Certificação_de_conhecimento.objects.get(id=certificacao_id)
    
    form = Form_certificação_de_conhecimento(request.POST or None, instance = certificacao)
    
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('certificacao_list'))
    
    requisitor = certificacao.requisitor
    
    print(requisitor)
    return render(request, 'certificacao.html' , {'certificacao': certificacao,
                                                    'form' : form})
    
class password_change(PasswordChangeView):
    template_name='registration/password_change.html'
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    
    
    def get(self, request, *args, **kwargs):
        
        user = request.user
        self.extra_context= {'user': user}
        
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        
        user = request.user
        self.extra_context= {'user': user}
        
        return super().post(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        form.save()
        user = self.request.user
        usuario = User.objects.filter(Q(id=user.id)).update(primeiro_login=False)
        
        try:
           for dados in usuario:
                dados.save()
        except:
            print(usuario)
            usuario 
            return redirect('http://127.0.0.1:8000/user/logout')            
            print('gg ;-;')
            
        # Updating the password logs out all other sessions for the user
        # except the current one.
        print(user.primeiro_login,'<<<<<<<<<<form')
        update_session_auth_hash(self.request, form.user)
        
        return super().form_valid(form)
 
from django.http import HttpResponseRedirect
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import PasswordChangeView 
from django.urls import reverse, reverse_lazy
from Users.forms import CustomUserCreateForm,  CustomUserChangeForm,  PasswordChangeForm
from django.shortcuts import render
from django.contrib.auth.models import Group
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
        print(usuario.curso_relacao.id, '<<<')
        
        teacher_group = Group.objects.get(name='Professor')
        
        teste =  professor.disciplina_relacao.all()
        
        for disciplinas in teste:
            for professor in disciplinas.banca_de_professores.all():
                print(professor.id, professor.username, 'user-', request.user.id)
                if professor.id == request.user.id:
                    print('GG')
        
        
        print(teste, '<')
        
        ###fix vvv
        
        banca_user = set()
        banca_disciplina = set()
        
        user = User.objects.get(id=request.user.id)
        disciplinas  = Disciplina.objects.all()
        
        for disciplina in disciplinas:
            print(disciplina.banca_de_professores.all())
            for professor in disciplina.banca_de_professores.all():
                print(professor.id,  professor.username)
                if professor.id == user.id:
                    print('GG')
                    banca_user.add(professor)
                    banca_disciplina.add(disciplina)
                    
        #fix
                  
        print(banca_disciplina, 'aaaaaaaaa')
            
        msg = 'Você não é Coordenador :p'
        teacher_group = Group.objects.get(name='Professor')
        certificacao = Certificação_de_conhecimento.objects.all()
        print(certificacao)
        
        for certificacoes in certificacao:
            print(certificacoes.disciplina, certificacoes.disciplina.banca_de_professores.all())
            for professor in certificacoes.disciplina.banca_de_professores.all():
                if professor.username == request.user.username:
                    print('GG  aq')
        
        
        return render(request, 'home_professor.html', { 'total_aproveitamentos': len(requisicoes_de_aproveitamento),
                                                        'aproveitamento': requisicoes_de_aproveitamento,
                                                        'total_certificacao' : len (requisicoes_de_certificacao),
                                                        'certificacao' : requisicoes_de_certificacao,
                                                        'coordenador': coordenador,
                                                        'usuario':usuario,
                                                        'Professor': teacher_group,
                                                        'disciplinas' : disciplinas,
                                                        'banca':banca_user,
                                                        'banca_disciplina':banca_disciplina,
                                                        'certificacao':certificacao})
    except:
        
        banca_user = set()
        banca_disciplina = set()
        
        user = User.objects.get(id=request.user.id)
        disciplinas  = Disciplina.objects.all()
        
        for disciplina in disciplinas:
            print(disciplina.banca_de_professores.all())
            for professor in disciplina.banca_de_professores.all():
                print(professor.id,  professor.username)
                if professor.id == user.id:
                    print('GG')
                    banca_user.add(professor)
                    banca_disciplina.add(disciplina)
                    
        print(banca_disciplina, 'aaaaaaaaa')
            
        coordenador = False
        msg = 'Você não é Coordenador :p'
        teacher_group = Group.objects.get(name='Professor')
        certificacao = Certificação_de_conhecimento.objects.all()
        print(certificacao)
        
        for certificacoes in certificacao:
            print(certificacoes.disciplina, certificacoes.disciplina.banca_de_professores.all())
            for professor in certificacoes.disciplina.banca_de_professores.all():
                if professor.username == request.user.username:
                    print('GG  aq')
            
        
        
        
        return render(request, 'home_professor.html', {'coordenador': coordenador,
                                                       'msg': msg,
                                                       'Professor': teacher_group,
                                                       'disciplinas' : disciplinas,
                                                       'banca':banca_user,
                                                       'banca_disciplina':banca_disciplina,
                                                       'certificacao':certificacao}) 
    
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


def lista_certificacao_professor (request, id):
    
    disciplina = Disciplina.objects.get(id=id)
    certificacao = Certificação_de_conhecimento.objects.all()
    certificacao_id = set()
    
    for certificacoes in certificacao:
        print(certificacoes.disciplina, certificacoes.disciplina.banca_de_professores.all())
        if certificacoes.disciplina.id == id:
            print(certificacoes.disciplina.id, certificacoes.requisitor, '<<<')
            certificacao_id.add(certificacoes)
            
    print(certificacao_id, '<<<<<<<<')
    
    return  render(request, 'certificacao_lista_professor.html', {'certificacoes':certificacao_id,
                                                                  'disciplina':disciplina})


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
    
    return  render(request, 'requisicoes_aproveitamento_lista.html', {'aproveitamento': requisicoes_de_aproveitamento,
                                                                      'len_aproveitamento': len(requisicoes_de_aproveitamento)})

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
    
    return  render(request, 'requisicoes_certificação_lista.html', {'certificacao': requisicoes_de_certificacao,
                                                                    'len_certificacao':len(requisicoes_de_certificacao)})

def iniciar_periodo_disciplina(request, disciplina_id):

    dados_disciplina = Disciplina.objects.get(id=disciplina_id)
    print(dados_disciplina)
    dependencias_disciplina = dados_disciplina.dependencia
    print(dependencias_disciplina)
    form = Form_disciplina_iniciar_perido_de_certificacao(request.POST or None, request.FILES or None, instance = dados_disciplina)

    if request.method == "POST":

        if form.is_valid():
            form.save()
            data = request.POST['data_final']
            print(data, '<<<<<')
            dados_disciplina = Disciplina.objects.filter(id=disciplina_id).update(aberto=True)       
            try:
                for objetos in dados_disciplina:
                    objetos.save()

            except:

                return redirect('sweet-home_teacher')   
    
    grupo_profesor = Group.objects.get(name='Professor')
    professores = User.objects.filter(groups=grupo_profesor)
    
    return render(request, 'iniciar_periodo_disciplina.html', {'disciplina':dados_disciplina,
                                                               'dependencias':dependencias_disciplina,
                                                               'professores' : professores,
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
        
        x = request.POST['status_requisição']
        print(x, '<<<<<<<<<<<<<<<<<<<<')
        form.save()
        
        if float(request.POST['nota']) > 100:
            certificacao = Certificação_de_conhecimento.objects.get(id=certificacao_id)
            certificacao.nota = 100
            certificacao.save()
            
        elif float(request.POST['nota']) < 0:
            certificacao = Certificação_de_conhecimento.objects.get(id=certificacao_id)
            certificacao.nota = 0
            certificacao.save()

        if request.POST['status_requisição'] == 'aprovado':
            certificacao = Certificação_de_conhecimento.objects.get(id=certificacao_id)
            certificacao.status_requisição = 'aguardo'
            certificacao.save()
                
        elif request.POST['status_requisição'] == 'reprovado':
            certificacao = Certificação_de_conhecimento.objects.get(id=certificacao_id)
            certificacao.status_requisição = 'aguardo'
            certificacao.nota = 0
            certificacao.save()
        
        fix = Certificação_de_conhecimento.objects.get(id=certificacao_id)
        disciplina = fix.disciplina.id
        
        return redirect('certificacao_list_professor', disciplina)
    
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
 
def search_aproveitamento (request, text):

    aproveitamento = Aproveitamento_de_disciplina.objects.filter(requisitor__username__contains=text)
    print(aproveitamento)
    return render(request, 'ajax/requisicoes_aproveitamento.html', {'aproveitamento': aproveitamento})

def search_certificacao (request, text):

    certificacao = Certificação_de_conhecimento.objects.filter(requisitor__username__contains=text)
    print(aproveitamento)
    return render(request, 'ajax/requisicoes_certificacao.html', {'certificacao': certificacao})
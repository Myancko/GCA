from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from administrador.models import Curso, Disciplina
from Aluno.models import Aproveitamento_de_disciplina, Certificação_de_conhecimento
from django.contrib.auth import get_user_model
from Aluno.form import Form_aproveitamento_de_disciplina, Form_certificação_de_conhecimento
from django.db.models import Q

User = get_user_model()

# Create your views here.

def home_professor (request):
    
    try:
        coordenador = True
        professor = User.objects.get(id=request.user.id)
        professor_curso_name = professor.curso_relacao
        professor_curso_disciplinas = professor.curso_relacao.disciplina.all()
        requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.all()
        requisicoes_de_certificacao = Certificação_de_conhecimento.objects.all()

        lista_de_disciplinas_curso = set()
        lista_de_disciplinas_curso2 = set()

        for dados in requisicoes_de_aproveitamento:
            print(dados, dados.disciplina.id, '<<')
            lista_de_disciplinas_curso.add(dados.disciplina.id)

        for dados in requisicoes_de_certificacao:
            print(dados, dados.disciplina.id, '<<')
            lista_de_disciplinas_curso2.add(dados.disciplina.id)
            
        for disciplnas in professor_curso_disciplinas.all():

            print(disciplnas, disciplnas.id, '<')


        requisicoes_de_aproveitamento = professor_curso_disciplinas.filter(id__in = lista_de_disciplinas_curso)
        requisicoes_de_certificacao = professor_curso_disciplinas.filter(id__in = lista_de_disciplinas_curso2)
        
        print(requisicoes_de_aproveitamento,'<<<<<')
        print(requisicoes_de_certificacao,'<<<<<')

        print(professor.id)
        print(professor_curso_name)
        print(professor_curso_disciplinas)

        print(requisicoes_de_aproveitamento,'<<')

        return render(request, 'home_professor.html', { 'total_aproveitamentos': len(requisicoes_de_aproveitamento),
                                                        'aproveitamento': requisicoes_de_aproveitamento,
                                                        'total_certificacao' : len (requisicoes_de_certificacao),
                                                        'certificacao' : requisicoes_de_certificacao,
                                                        'coordenador': coordenador})
    except:
        coordenador = False
        msg = 'Você não é Coordenador :p'
        return render(request, 'home_professor.html', {'coordenador': coordenador,
                                                       'msg': msg}) 
    
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

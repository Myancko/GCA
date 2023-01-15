from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from administrador.models import Curso, Disciplina

# Create your views here.

@login_required(login_url='/user/login/')
def home_aluno (request):
    
    aluno = request.user
    aluno_curso = aluno.curso_relacao.id
    
    print(aluno_curso)
    
    print(aluno.is_superuser , '<<<<<<<<<<<')
    
    nome_do_aluno_logado = aluno.username 
    curso_do_aluno = aluno.curso_relacao
    
    return render(request, 'home_student.html', {'username' : nome_do_aluno_logado,
                                                 'curso' : curso_do_aluno,
                                                 'aluno_dados' : aluno})
    #return HttpResponse("teste")
  
@login_required(login_url='/user/login/')  

def aluno_curso (request, curso_id):
    
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
    
    return  render (request, 'vizualizar_dados.html', {'curso': curso,
                                                       'disciplinas' : m2m,
                                                       'total_disciplinas' : len_disciplinas,
                                                       'total_de_optativas': len_optativas,
                                                       'total_de_nao_optativas' : len_nao_opttivas})

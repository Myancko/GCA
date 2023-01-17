from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from administrador.models import Curso, Disciplina
from django.contrib import messages
from  .form import Form_aproveitamento_de_disciplina,Form_certificação_de_conhecimento 
from .models import Aproveitamento_de_disciplina, Certificação_de_conhecimento

from django.views.generic.edit import CreateView
# Create your views here.

@login_required(login_url='/user/login/')
def home_aluno (request):
    
    aluno = request.user
    try:
        aluno_curso = aluno.curso_relacao.id
    except:
        aluno_curso = None

    
    x = request.user.image.url
    print(request.user.image.url, '<<<<<<<<')
    
    print(aluno_curso)
    
    print(aluno.is_superuser , '<<<<<<<<<<<')
    
    nome_do_aluno_logado = aluno.username 
    curso_do_aluno = aluno.curso_relacao
    
    return render(request, 'home_student.html', {'username' : nome_do_aluno_logado,
                                                 'curso' : curso_do_aluno,
                                                 'aluno_dados' : aluno,
                                                 'img_link':x})
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
    
def modal_selecionarAC (request):
    
    return render (request, 'modais/teste.html', {})

def modal_menu (request):
    
    return render (request, 'modais/modal_menu.html', {})

""" class requisitar_aproveitamento_de_disciplina_class(CreateView):
    form_class  = Form_aproveitamento_de_disciplina
    success_url = reverse_lazy('sweet_home')
    template_name = 'requisitar_aproveitamento_de_disciplina.html'
    model = Aproveitamento_de_disciplina
    

    def form_valid(self, form):
        response = super().form_valid(form)
         form.save_m2m() 
        
        messages.success(self.request, "Requisição realizada com sucesso")
        return response """
        
def requisitar_aproveitamento_de_disciplina (request, disciplina_id):
    
    disciplina = Disciplina.objects.all()
    disciplina_requisição = Disciplina.objects.get(id=disciplina_id)
    form = Form_aproveitamento_de_disciplina() 
    
    if request.method == "POST":
        form = Form_aproveitamento_de_disciplina(request.POST, request.FILES)
        print("#########")
        print(form.errors)
        print(form)
        print(request.POST['disciplina'], '<<<<')
        if form.is_valid():

            #file_two = Aproveitamento_de_disciplina( comprovante = request.FILES['comprovante'])
            print('ok')
            form.save()
            return HttpResponseRedirect(reverse('home'))
        else:
            return render(request, 'requisitar_aproveitamento_de_disciplina.html', {'disciplina': disciplina,
                'disciplina_requisição' : disciplina_requisição,
                'form':  form}  )
    
    else: 
        context = {'disciplina': disciplina,
                'disciplina_requisição' : disciplina_requisição,
                'form':  form}  

        return render (request, 'requisitar_aproveitamento_de_disciplina.html', context)
    

class requisitar_certificacao_de_conhecimento_class(CreateView):
    form_class  = Form_certificação_de_conhecimento
    success_url = reverse_lazy('sweet_home')
    template_name = 'requisitar_certificação_de_conhecimento.html'
    model = Certificação_de_conhecimento
        

    def get(self, request, *args, **kwargs) -> HttpResponse:
        print(kwargs['disciplina_id'], "<<<<<")

        disciplina = Disciplina.objects.all()
        disciplina_requisição = Disciplina.objects.get(id=kwargs['disciplina_id'])

        self.extra_context= {'disciplina': disciplina_requisição}
        return super().get(request, *args, **kwargs)
    

def requisitar_certificacao_de_conhecimento (request, disciplina_id):
    
    return render (request, 'requisitar_certificação_de_conhecimento.html', {})
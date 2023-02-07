from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.contrib.auth import update_session_auth_hash
from administrador.models import Curso, Disciplina
from django.contrib import messages
from Users.forms import CustomUserCreateForm,  CustomUserChangeForm,  PasswordChangeForm
from .form import Form_aproveitamento_de_disciplina,Form_certificação_de_conhecimento
from .models import Aproveitamento_de_disciplina, Certificação_de_conhecimento
from django.contrib.auth.views import PasswordChangeView 
#from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect
from django.db.models import Q
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views.generic.edit import CreateView
from datetime import date, timedelta
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import LoginRequiredMixin

dia_de_hj = date.today()


@login_required(login_url='/user/login/')
def home_aluno (request):
    
    aluno = request.user
    try:
        aluno_curso = aluno.curso_relacao.id
    except:
        aluno_curso = None

    print('primeiro_login =',aluno.primeiro_login, '<<<<<<<')
    
    if aluno.primeiro_login == True:
        
        primeiro_login = redirect ('/Aluno/aluno_home/alterar_senha/', {})
        return primeiro_login
    
    x = request.user.image.url
    print(request.user.image.url, '<<<<<<<<')
    
    print(aluno_curso)
    
    print(aluno.is_superuser , '<<<<<<<<<<<')
    
    nome_do_aluno_logado = aluno.username 
    curso_do_aluno = aluno.curso_relacao
    
    requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.filter(requisitor=aluno.id).count()
    
    
    return render(request, 'home_student.html', {'username' : nome_do_aluno_logado,
                                                 'curso' : curso_do_aluno,
                                                 'aluno_dados' : aluno,
                                                 'numero_requisicoes_aproveitamento' : requisicoes_de_aproveitamento,
                                                 'img_link':x})
    #return HttpResponse("teste")
  
@login_required(login_url='/user/login/')  

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
    
@login_required(login_url='/user/login/')
def vizualizar_minhas_requisicoes_de_aproveitamento (request):
    
    aluno = request.user
    requisicoes_de_aproveitamento = Aproveitamento_de_disciplina.objects.filter(requisitor=aluno.id)
    
    curso  = Curso.objects.get(id=aluno.curso_relacao.id)
    m2m  = curso.disciplina.all()
    len_disciplinas = len(curso.disciplina.all())
    
    len_optativas = 0
    len_nao_opttivas = 0
    
    for disciplina in m2m:
        if disciplina.optativa == 'S':
            len_optativas  +=1
        else:
            len_nao_opttivas += 1
    
    return render (request, 'vizualizar_minhas_requisicoes_aproveitamento.html', {'requisicoes_de_aproveitamento':requisicoes_de_aproveitamento,
                                                                                  'total_requisicoes_aproveitamento':len(requisicoes_de_aproveitamento),
                                                                                  'curso':curso,
                                                                                  'total_disciplinas' : len_disciplinas,
                                                                                  'total_de_optativas': len_optativas,
                                                                                  'total_de_nao_optativas' : len_nao_opttivas})

@login_required(login_url='/user/login/')
def vizualizar_minhas_requisicoes_de_certificacao (request):
    
    aluno = request.user
    requisicoes_de_certificacao = Certificação_de_conhecimento.objects.filter(requisitor=aluno.id)
    
    curso  = Curso.objects.get(id=aluno.curso_relacao.id)
    m2m  = curso.disciplina.all()
    len_disciplinas = len(curso.disciplina.all())
    
    len_optativas = 0
    len_nao_opttivas = 0
    
    for disciplina in m2m:
        if disciplina.optativa == 'S':
            len_optativas  +=1
        else:
            len_nao_opttivas += 1
    return render (request, 'vizualizar_minhas_requisicoes_certificacao.html', {'requisicoes_de_certificacao':requisicoes_de_certificacao,
                                                                                'total_requisicoes_certificacao':len(requisicoes_de_certificacao),
                                                                                'curso':curso,
                                                                                'total_disciplinas' : len_disciplinas,
                                                                                'total_de_optativas': len_optativas,
                                                                                'total_de_nao_optativas' : len_nao_opttivas})

@login_required(login_url='/user/login/')      
def requisitar_aproveitamento_de_disciplina (request, disciplina_id):
    
    
    disciplina = Disciplina.objects.all()
    disciplina_requisição = Disciplina.objects.get(id=disciplina_id)
    aluno = request.user
    
    for disiciplina in aluno.disciplina_concluidas.all():
        
        if disiciplina == disciplina_requisição:
            
            messages.warning(request, 'Você já Cursou a Disciplina ' + str( disiciplina.nome ))
            return redirect('curso_aluno', aluno.curso_relacao.id ) 
            input()
    

    try:
        verificar = Certificação_de_conhecimento.objects.get(disciplina=disciplina_requisição, requisitor=request.user.id )
        print(verificar, '<<<<')
        messages.warning(request, 'Você já iniciou uma requisição de certificacao de conhecimento para a disciplina ' + str( disiciplina.nome ) +
                         ' \ne não pode iniciar uma requisição de aproveitamento de disciplina.')
        return redirect('curso_aluno', aluno.curso_relacao.id ) 
    
    except:
        
        dependencias = 0  
        concluidas = 0 
        for dependencia in disciplina_requisição.dependencia.all():
            #verificar dependencias
            dependencias += 1 
            for diciplinas_concluida in aluno.disciplina_concluidas.all():
                if dependencia == diciplinas_concluida:
                    concluidas  +=1
                    
        print(dependencias, concluidas, '<<<')
        if dependencias == concluidas:
            print('pd passar')
            print(dependencias, concluidas, '<<<')
        else:
            messages.warning(request, 'Você não tem as dependencias da disciplina  ' + str( disciplina_requisição.nome ))
            return redirect('curso_aluno', aluno.curso_relacao.id ) 
        
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
    

class requisitar_certificacao_de_conhecimento_class(LoginRequiredMixin, CreateView):
    form_class  = Form_certificação_de_conhecimento
    success_url = reverse_lazy('sweet_home')
    template_name = 'requisitar_certificação_de_conhecimento.html'
    model = Certificação_de_conhecimento
    

    def get(self, request, *args, **kwargs) -> HttpResponse:
        
        print(kwargs['disciplina_id'], "<<<<<")
        user = request.user

        disciplina = Disciplina.objects.all()
        disciplina_requisição = Disciplina.objects.get(id=kwargs['disciplina_id'])
        print(dia_de_hj+timedelta(days=10), '<<<<<<< aq')
        
        try:
            #verificar  se  aproveitamento  de disciplina da msm disciplina existe
            verificar = Aproveitamento_de_disciplina.objects.get(disciplina=disciplina_requisição, requisitor=request.user.id )
            print(verificar, '<<<<')
            messages.warning(request, 'Você já iniciou uma requisição de Aproveitamento de disciplina para a disciplina ' + str( disiciplina.nome ) +
                             ' \ne não pode iniciar uma requisição de Certificacao de conhecimento.')
            return redirect('curso_aluno', user.curso_relacao.id ) 
        
        except:
        
            for disiciplina in user.disciplina_concluidas.all():
            #verifica se a disciplina não foi concluida
                    if disiciplina == disciplina_requisição:

                        messages.warning(request, 'Você já Cursou a Disciplina ' + str( disiciplina.nome ))
                        return redirect('curso_aluno', user.curso_relacao.id ) 

            dependencias = 0  
            concluidas = 0 

            for dependencia in disciplina_requisição.dependencia.all():
                #verificar dependencias
                dependencias += 1 
                for diciplinas_concluida in user.disciplina_concluidas.all():
                    if dependencia == diciplinas_concluida:
                        concluidas  +=1

            print(dependencias, concluidas, '<<<')
            if dependencias == concluidas:
                print('pd passar')
                print(dependencias, concluidas, '<<<')
            else:
                messages.warning(request, 'Você não tem as dependencias da disciplina  ' + str( disciplina_requisição.nome ))
                return redirect('curso_aluno', user.curso_relacao.id ) 

            if disciplina_requisição.aberto == True and disciplina_requisição.data_final >= dia_de_hj:
                self.extra_context= {'disciplina': disciplina_requisição}
                return super().get(request, *args, **kwargs)

            else:

                if disciplina_requisição.aberto == False:
                    messages.error(request, 'O perido para a requisição de certificação de conhecimento da disciplina '+ '\''+str(disciplina_requisição.nome)+'\''+
                                    ' Não foi iniciado.')

                    return redirect('curso_aluno', user.curso_relacao.id ) 

                elif disciplina_requisição.data_final < dia_de_hj:
                    messages.error(request, 'O perido para as requisições de certificação de conhecimento da disciplina '+ '\''+str(disciplina_requisição.nome)+'\''+
                                    ' expirou no dia '+str(disciplina_requisição.data_final.day)+
                                                     '/'+str(disciplina_requisição.data_final.month)+
                                                     '/'+str(disciplina_requisição.data_final.year) )

                    return redirect('curso_aluno', user.curso_relacao.id ) 

                else:
                    messages.error(request, 'Ocorreu algum erro por favor entre em contato com o administrador do sistema')
                    return redirect('sweet_home') 

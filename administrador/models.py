from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Disciplina (models.Model):

    OPTATIVA = (
        ("S", "Sim"),
        ("N", "Não"),
    )
    
    STATUS = (
        ("Cursando", "Cursando"),
        ("Aprovado", "Aprovado"),
        ("Espera", "Espera")
    )
    
    nome = models.CharField(("Nome da Disciplina"), max_length=150, null=False)
    perido = models.IntegerField(("Periodo da disciplina"))
    carga_horaria = models.IntegerField(("Carga Horaria"))
    optativa = models.CharField(("Opitativa"), choices=OPTATIVA, blank=False, null=False,max_length=20)
    dependencia = models.ManyToManyField("self", verbose_name=("Dependencias"), blank=True, default='Sem Dependencia')
    aberto = models.BooleanField(("Aberto"), default='False')
    status = models.CharField('Status', choices=STATUS, max_length=20, default="Cursando")
    data_final = models.DateField(("Data Final"), blank=True, null=True,auto_now=False, auto_now_add=False)
    
    pedagogo = models.ForeignKey (User, verbose_name=("pedagogo"), on_delete=models.CASCADE, related_name='pedagogo', blank=True, null=True)
    banca_de_professores = models.ManyToManyField(User, verbose_name=("Banca de professores"), related_name='professores', blank=True, null=True)
    
    verbose_name = 'Disciplina'
    verbose_name_plural = 'Disciplinas'
    
    def __str__(self):
        return self.nome +' '+ str(self.perido) 
    
class Curso (models.Model):
    
    nome = models.CharField(("Nome do Curso"), max_length=150, null=False, blank=False)
    ano = models.DateField("Ano")
    periodos =  models.IntegerField(('Total de peridodos'), null=False, blank=False)
    #periodo_atual = models.IntegerField(('Total de peridodos'), null=True, blank=True)
    disciplina = models.ManyToManyField("administrador.Disciplina", verbose_name=("Disciplinas"),blank=False)
    
    coordenador = models.ForeignKey(User, verbose_name=("Coordenador"), on_delete=models.SET_NULL, null=True)
    
    
    verbose_name = 'Curso'
    verbose_name_plural = 'Cursos'
    
    def __str__(self):
        return self.nome +' ('+ str(self.ano.year) +')'
    
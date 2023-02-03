from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.

class Aproveitamento_de_disciplina (models.Model):
    
    STATUS = (
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("aguardo", "Aguardo")
    )

    disciplina =  models.ForeignKey('administrador.Disciplina', on_delete=models.CASCADE)
    motivo = models.CharField("Motivo", max_length=250, blank=True, null=True)
    historico = models.FileField(("Historico"), upload_to='documentos', max_length=1000)
    comprovante = models.FileField(("Comprovante"), upload_to='documentos', max_length=1000)
    status_requisição = models.CharField(("Status"), choices=STATUS, blank=False, null=False, max_length=20,  default='reprovado')
    requisitor =  models.ForeignKey(User, verbose_name=("Requisitor"), on_delete=models.CASCADE, blank=False, null=False)
 
    verbose_name = 'Aproveitamento de disciplina'
    verbose_name_plural = 'Aproveitamentos de disciplina'
    
    class Meta:
      db_table = 'Aluno_aproveitamento_de_disciplina'
      unique_together = (('disciplina', 'requisitor'),)
    
    def __str__(self):
        return self.disciplina.nome +' '+ self.requisitor.username
    
    
    
class Certificação_de_conhecimento (models.Model):
    
    STATUS = (
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("aguardo", "Aguardo")
    )

    disciplina =  models.ForeignKey('administrador.Disciplina', on_delete=models.CASCADE)
    status_requisição = models.CharField(("Status"), choices=STATUS, blank=False, null=False, max_length=20,  default='reprovado')
    nota = models.FloatField(("Nota"), blank=True, null=True, default=0)
    pedagogo = models.ForeignKey (User, verbose_name=("pedagogo"), on_delete=models.CASCADE, related_name='pedagogo', blank=True, null=True)
    banca_de_professores = models.ManyToManyField(User, verbose_name=("Professores"), related_name='professores', blank=True, null=True)
    requisitor =  models.ForeignKey(User, verbose_name=("Requisitor"), on_delete=models.CASCADE, blank=False, null=False)

    verbose_name = 'Certificação de conhecimento'
    verbose_name_plural = 'Certificações de conhecimento'
    
    class Meta:
      db_table = 'Aluno_certificação_de_conhecimento'
      unique_together = (('requisitor', 'disciplina'),)
    
    def __str__(self):
        return self.disciplina.nome +' '+ self.requisitor.username
    
    
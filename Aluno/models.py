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
    status_requisição = models.CharField(("Opitativa"), choices=STATUS, blank=False, null=False, max_length=20,  default='reprovado')
    requisitor =  models.OneToOneField(User, verbose_name=("Requisitor"), on_delete=models.CASCADE, blank=False, null=False)
 
    verbose_name = 'Disciplina'
    verbose_name_plural = 'Disciplinas'
    
    def __str__(self):
        return self.nome +' '+ str(self.perido) 
    
    
    
class Certificação_de_conhecimento (models.Model):
    
    STATUS = (
        ("aprovado", "Aprovado"),
        ("reprovado", "Reprovado"),
        ("aguardo", "Aguardo")
    )

    disciplina =  models.ForeignKey('administrador.Disciplina', on_delete=models.CASCADE)
    status_requisição = models.CharField(("Opitativa"), choices=STATUS, blank=False, null=False, max_length=20,  default='reprovado')
    nota = models.FloatField(("Nota"))
    requisitor =  models.OneToOneField(User, verbose_name=("Requisitor"), on_delete=models.CASCADE, blank=False, null=False)

    verbose_name = 'Disciplina'
    verbose_name_plural = 'Disciplinas'
    
    def __str__(self):
        return self.nome +' '+ str(self.perido) 
    
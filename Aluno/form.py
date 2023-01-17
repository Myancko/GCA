from django import forms
from django.forms import ModelForm
from .models import  Aproveitamento_de_disciplina, Certificação_de_conhecimento


class Form_aproveitamento_de_disciplina (ModelForm):
    
    erro_css_class = 'erro-field'
    required_css_class= 'disciplina-fields'
    
    class Meta:
        model = Aproveitamento_de_disciplina
        fields = 'disciplina', 'motivo', 'historico', 'comprovante', 'status_requisição', 'requisitor'



class Form_certificação_de_conhecimento (ModelForm):
    
    erro_css_class = 'erro-field'
    required_css_class= 'disciplina-fields'
    
    class Meta:
        model = Certificação_de_conhecimento
        fields = 'disciplina','status_requisição','nota','requisitor'
    
        
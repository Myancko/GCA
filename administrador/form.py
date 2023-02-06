from django import forms
from django.forms import ModelForm
from .models import Disciplina, Curso

class DateInput(forms.DateInput):
    input_type = 'date'

class Form_disciplina (ModelForm):
    
    erro_css_class = 'erro-field'
    required_css_class= 'disciplina-fields'
    
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "nome"}))
    #perido = forms.CharField(widget=forms.IntegerField(attrs={"class": "nome"}))
    
    CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
    )

    
    optativa = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES )

         
    class Meta:
        model = Disciplina
        fields = 'nome', 'perido', 'carga_horaria', 'optativa', 'dependencia'

    def __init__  (self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['nome'].label =  ''
        self.fields['nome'].widget.attrs.update({'class': 'nome_perido', 'placeholder': 'Nome' })
        
        self.fields['perido'].label =  ''
        self.fields['perido'].widget.attrs.update({'class': 'perido', 'placeholder': 'Perido'} )
        
        self.fields['carga_horaria'].label =  ''
        self.fields['carga_horaria'].widget.attrs.update({'class': 'carga_horaria', 'placeholder': 'Carga Horaria da Disciplina' })
        
        #self.fields['optativa'].label =  ''    
        self.fields['optativa'].widget.attrs.update({'class': 'optativa','placeholder': 'optativa'})
        
        self.fields['dependencia'].widget.attrs.update({'class': 'dependencia', 'placeholder': 'dependencia'})


class Form_Curso (ModelForm):
    
    erro_css_class = 'erro-field'
    required_css_class= 'disciplina-fields'
    
    ano = forms.DateField(widget=DateInput)
    
    class Meta:
        model = Curso
        fields = 'nome','ano','periodos','disciplina','coordenador'
    
    def __init__  (self, *args, **kargs):
        super().__init__(*args, **kargs)

        self.fields['nome'].label =  ''
        self.fields['nome'].widget.attrs.update({'class': 'nome_curso', 'placeholder': 'Nome' })

        self.fields['ano'].label =  ''
        self.fields['ano'].widget.attrs.update({'class': 'ano', 'placeholder': 'Ano > MM/DD/AAAA'} )
        
        self.fields['periodos'].label =  ''
        self.fields['periodos'].widget.attrs.update({'class': 'periodos', 'placeholder': 'Total de Periodos do Curso'} )
        
        self.fields['disciplina'].label =  'Escolha as Disciplinas do Curso'
        self.fields['disciplina'].widget.attrs.update({'class': 'disciplina', 'placeholder': 'Disciplinas do Curso'} )
        
        self.fields['coordenador'].label =  'Escolha o Coordenador do Curso'
        self.fields['coordenador'].widget.attrs.update({'class': 'coordenador', 'placeholder': 'Coordenador do Curso'} )
        
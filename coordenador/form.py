from django import forms
from django.forms import ModelForm
from administrador.models import Disciplina
from datetime import date
from django.contrib.admin.widgets import AdminDateWidget
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
data_de_hoje = date.today()

class DateInput(forms.DateInput):
    input_type = 'date'


class Form_disciplina_iniciar_perido_de_certificacao (ModelForm):
    
    erro_css_class = 'erro-field'
    required_css_class= 'disciplina-fields'
    
    nome = forms.CharField(widget=forms.TextInput(attrs={"class": "nome"}))
    data_final = forms.DateField(widget=DateInput)
    #perido = forms.CharField(widget=forms.IntegerField(attrs={"class": "nome"}))
    
    CHOICES = (
        ("S", "Sim"),
        ("N", "Não"),
    )

    grupo_profesor = Group.objects.get(name='Pedagogo')
    professores = User.objects.filter(groups=grupo_profesor)
    
    optativa = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES )
    pedagogo = forms.ModelChoiceField(required=True,  queryset=professores)
    
    class Meta:
        model = Disciplina
        fields = 'nome', 'perido', 'carga_horaria', 'optativa', 'dependencia', 'aberto', 'data_final', 'banca_de_professores', 'pedagogo'

    def __init__  (self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.fields['nome'].label =  ''
        self.fields['nome'].widget.attrs.update({'class': 'nome_perido', 'placeholder': 'Nome', 'readOnly': 'true' })
        
        self.fields['data_final'].label =  ''
        self.fields['data_final'].widget.attrs.update({'class': 'data_final', 'min':data_de_hoje })
        
        self.fields['aberto'].label =  ''
        self.fields['aberto'].widget.attrs.update({'class': 'disciplina_requisicao', 'placeholder': 'Status da disciplina' })
        
        self.fields['perido'].label =  ''
        self.fields['perido'].widget.attrs.update({'class': 'perido', 'placeholder': 'Perido', 'readOnly': 'true'} )
        
        self.fields['carga_horaria'].label =  ''
        self.fields['carga_horaria'].widget.attrs.update({'class': 'carga_horaria', 'placeholder': 'Carga Horaria da Disciplina', 'readOnly': 'true' })
        
        #self.fields['optativa'].label =  ''    
        self.fields['optativa'].widget.attrs.update({'class': 'optativa','placeholder': 'optativa', 'readOnly': 'true'})
        
        self.fields['dependencia'].widget.attrs.update({'class': 'dependencia', 'placeholder': 'dependencia'})
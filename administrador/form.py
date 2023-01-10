from django import forms
from django.forms import ModelForm
from .models import Disciplina, Curso


class Form_disciplina (ModelForm):
    class Meta:
        model = Disciplina
        fields = '__all__'


class Form_Curso (ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'
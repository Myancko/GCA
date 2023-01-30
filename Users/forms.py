from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm
from django.contrib.auth import password_validation
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.core.exceptions import ValidationError

from .models import CustomUser
from django.contrib import messages


class CustomUserCreateForm(UserCreationForm):
    #REQUIRED_FIELDS = ['matricula','username' , 'email' ,'cpf', 'phone']
    error_messages = {
        'password_mismatch': 'Type smtn here!',
    }
    class Meta:
        
        model = CustomUser
        fields = ( 'image','matricula','username' , 'email' ,'cpf', 'phone', 'data_de_nascimento','curso_relacao','disciplina_relacao','password1','password2')

    def __init__  (self, *args, **kargs):
        self.error_messages['password_mismatch'] = 'Type smtn here!'
        super().__init__(*args, **kargs)
        
        self.fields['image'].label =  ''
        self.fields['image'].widget.attrs.update({'class': 'image', 'placeholder': 'Image' })
        
        self.fields['matricula'].label =  ''
        self.fields['matricula'].widget.attrs.update({'class': 'matricula', 'placeholder': 'Matricula' })
    
        self.fields['username'].label =  ''
        self.fields['username'].widget.attrs.update({'class': 'username', 'placeholder': 'Nome' })
        
        self.fields['email'].label =  ''
        self.fields['email'].widget.attrs.update({'class': 'email', 'placeholder': 'E-mail' })
        
        self.fields['cpf'].label =  ''
        self.fields['cpf'].widget.attrs.update({'class': 'cpf', 'placeholder': 'CPF' })
        
        self.fields['phone'].label =  ''
        self.fields['phone'].widget.attrs.update({'class': 'phone', 'placeholder': 'Telefone' }) 
        
        self.fields['data_de_nascimento'].label =  ''
        self.fields['data_de_nascimento'].widget.attrs.update({'class': 'data_de_nascimento', 'placeholder': 'data_de_nascimento > MM/DD/AAAA' })   
        
        self.fields['curso_relacao'].label =  'Curso a Coordenar'
        self.fields['curso_relacao'].widget.attrs.update({'class': 'curso_relacao', 'placeholder': 'curso' })      
        
        self.fields['disciplina_relacao'].label =  'Disciplinas a Lecionar'
        self.fields['disciplina_relacao'].widget.attrs.update({'class': 'disciplina_relacao', 'placeholder': 'disciplina' })      
        
        self.fields['password1'].label =  ''
        self.fields['password1'].widget.attrs.update({'class': 'password1', 'placeholder': 'Senha' })      
        
        self.fields['password2'].label =  ''
        self.fields['password2'].widget.attrs.update({'class': 'password2', 'placeholder': 'Confirme a Senha' })    
         
        def save(self, commit=True):
            
            
            user: CustomUser = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.image = self.cleaned_data["image"]
            user.data_de_nascimento = self.cleaned_data["data_de_nascimento"]
            user.matricula = self.cleaned_data["matricula"]
            user.username = self.cleaned_data["username"]
            user.email = self.cleaned_data["email"]
            user.cpf = self.cleaned_data["cpf"]
            user.phone = self.cleaned_data["phone"]
            user.curso_relacao = self.cleaned_data["curso_relacao"]
            user.disciplina_relacao = user.disciplina_relacao
            
            #user.first_name = self.cleaned_data["first_name"]
            #user.last_name = self.cleaned_data["last_name"]
            #user.username = user.email
            if commit:

                print(user.disciplina_relacao)
                user.save()

            return user

class CustomUserChangeForm(UserChangeForm):
    error_messages = {
        'password_mismatch': 'Type smtn here!',
    }

    class Meta:
        model = CustomUser
        fields = ('image','matricula','username' , 'email' ,'cpf', 'phone', 'data_de_nascimento','curso_relacao','disciplina_relacao')
        
    def __init__  (self, *args, **kargs):
        self.error_messages['password_mismatch'] = 'Type smtn here!'
        super().__init__(*args, **kargs)
        
        self.fields['image'].label =  ''
        self.fields['image'].widget.attrs.update({'class': 'image', 'placeholder': 'Image' })
        
        self.fields['matricula'].label =  ''
        self.fields['matricula'].widget.attrs.update({'class': 'matricula', 'placeholder': 'Matricula', 'readonly':'readonly' })
    
        self.fields['username'].label =  ''
        self.fields['username'].widget.attrs.update({'class': 'username', 'placeholder': 'Nome' })
        
        self.fields['email'].label =  ''
        self.fields['email'].widget.attrs.update({'class': 'email', 'placeholder': 'E-mail' })
        
        self.fields['cpf'].label =  ''
        self.fields['cpf'].widget.attrs.update({'class': 'cpf', 'placeholder': 'CPF' })
        
        self.fields['phone'].label =  ''
        self.fields['phone'].widget.attrs.update({'class': 'phone', 'placeholder': 'Telefone' }) 
        
        self.fields['data_de_nascimento'].label =  ''
        self.fields['data_de_nascimento'].widget.attrs.update({'class': 'data_de_nascimento', 'placeholder': 'data_de_nascimento > MM/DD/AAAA' })   
        
        self.fields['curso_relacao'].label =  'Curso a Coordenar'
        self.fields['curso_relacao'].widget.attrs.update({'class': 'curso_relacao', 'placeholder': 'curso' })      
        
        self.fields['disciplina_relacao'].label =  'Disciplinas a Lecionar'
        self.fields['disciplina_relacao'].widget.attrs.update({'class': 'disciplina_relacao', 'placeholder': 'disciplina' })  


class CustomUserChangeForm_Config(UserChangeForm):
    error_messages = {
        'password_mismatch': 'Type smtn here!',
    }

    class Meta:
        model = CustomUser
        fields = ('image','matricula','username','email','cpf','phone','data_de_nascimento','curso_relacao','disciplina_relacao')
        
    def __init__  (self, *args, **kargs):
        self.error_messages['password_mismatch'] = 'Type smtn here!'
        super().__init__(*args, **kargs)
        
        self.fields['image'].label =  ''
        self.fields['image'].widget.attrs.update({'class': 'image', 'placeholder': 'Image' })
        
        self.fields['matricula'].label =  ''
        self.fields['matricula'].widget.attrs.update({'class': 'matricula', 'placeholder': 'Matricula', 'readonly':'readonly' })
    
        self.fields['username'].label =  ''
        self.fields['username'].widget.attrs.update({'class': 'username', 'placeholder': 'Nome' })
        
        self.fields['email'].label =  ''
        self.fields['email'].widget.attrs.update({'class': 'email', 'placeholder': 'E-mail' })
        
        self.fields['cpf'].label =  ''
        self.fields['cpf'].widget.attrs.update({'class': 'cpf', 'placeholder': 'CPF', 'readonly':'readonly'  })
        
        self.fields['phone'].label =  ''
        self.fields['phone'].widget.attrs.update({'class': 'phone', 'placeholder': 'Telefone' }) 
        
        self.fields['data_de_nascimento'].label =  ''
        self.fields['data_de_nascimento'].widget.attrs.update({'class': 'data_de_nascimento', 'placeholder': 'data_de_nascimento > MM/DD/AAAA' })   
        
        self.fields['curso_relacao'].label =  'Curso a Coordenar'
        self.fields['curso_relacao'].widget.attrs.update({'class': 'curso_relacao', 'placeholder': 'curso', 'readonly':'readonly'  })      
        
        self.fields['disciplina_relacao'].label =  'Disciplinas a Lecionar'
        self.fields['disciplina_relacao'].widget.attrs.update({'class': 'disciplina_relacao', 'placeholder': 'disciplina', 'readonly':'readonly' })  


class SetPasswordForm(forms.Form):
    """
    A form that lets a user change set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": ("As senhas não coincidem."),
    }
    new_password1 = forms.CharField(
        label=("Nova senha"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("Confirme a nova senha"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2:
            if password1 != password2:
                raise ValidationError(
                    self.error_messages["password_mismatch"],
                    code="password_mismatch",
                )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


class PasswordChangeForm(SetPasswordForm):


    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": (
            "A sua senha antiga esta incorreta. Por favor insira novamente."
        ),
    }
    old_password = forms.CharField(
        label=("Senha Antiga"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm , AuthenticationForm

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

from .models import CustomUser
from django.contrib import messages


class CustomUserCreateForm(UserCreationForm):
    #REQUIRED_FIELDS = ['matricula','username' , 'email' ,'cpf', 'phone']
    class Meta:
        model = CustomUser

        fields = ( 'matricula','username' , 'email' ,'cpf', 'phone', 'first_name', 'last_name','is_staff','is_superuser')
        
        def save(self, commit=True):
            
            
            user: CustomUser = super().save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            user.matricula = self.cleaned_data["matricula"]
            user.username = self.cleaned_data["username"]
            user.email = self.cleaned_data["email"]
            user.cpf = self.cleaned_data["cpf"]
            user.phone = self.cleaned_data["phone"]
            #user.first_name = self.cleaned_data["first_name"]
            #user.last_name = self.cleaned_data["last_name"]
            #user.username = user.email
            if commit:

                user.save()

            return user


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'phone', 'first_name', 'last_name')
        

   

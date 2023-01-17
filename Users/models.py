from django.db import models
from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractUser
from django.db.models import signals

# Create your models here.

class UserManager(BaseUserManager):
    #REQUIRED_FIELDS = ['matricula','username' , 'email' ,'cpf', 'phone']

    def _create_user(self, image,  matricula, username, email, cpf,  phone, data_de_nascimento, disciplina_relacao, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not matricula:
           raise ValueError("O matricula é obrigatório")
        if not username:
           raise ValueError("O username é obrigatório")
        if not cpf:
           raise ValueError("O cpf é obrigatório")
        if not phone:
            raise ValueError("O phone é obrigatório")
        
        email = self.normalize_email(email)
        
        """ username = seusername
        matricula = seemail """
        
        user = self.model(image=image, matricula=matricula, username=username, email=email, cpf=cpf, phone=phone, data_de_nascimento=data_de_nascimento, disciplina_relacao=disciplina_relacao, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def _create_super_user(self,  matricula, username, email, cpf,  phone, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")
        if not matricula:
           raise ValueError("O matricula é obrigatório")
        if not username:
           raise ValueError("O username é obrigatório")
        if not cpf:
           raise ValueError("O cpf é obrigatório")
        if not phone:
            raise ValueError("O phone é obrigatório")
        
        email = self.normalize_email(email)
        
        """ username = seusername
        matricula = seemail """
        
        user = self.model(matricula=matricula, username=username, email=email, cpf=cpf, phone=phone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, image, matricula, username, email, cpf,  phone, data_de_nascimento=None, disciplina_relacao=None,password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', True)
        return self._create_user( image, matricula, username, email, cpf,  phone, data_de_nascimento, disciplina_relacao, password, **extra_fields)

    def create_superuser(self, matricula, username, email, cpf, phone, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser = True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff = True')

        return self._create_super_user( matricula, username, email, cpf,  phone, password, **extra_fields)



class CustomUser(AbstractUser):


    image = models.ImageField(upload_to='Media', blank=True, null=False, default='Media/no_image_dafaut.jpg')
    matricula = models.CharField("Matricula", max_length=150, unique=True)
    username = models.CharField(("Nome"), max_length=50, unique=False, primary_key=None)
    email = models.EmailField("E-mail", unique=True)
    cpf = models.CharField("CPF", max_length=14, unique=True)
    phone = models.CharField("Telefone", max_length=15, blank=True, null=True)
    data_de_nascimento = models.DateField('Data de Nascimento', blank=True, null=True)
    
    
    curso_relacao = models.ForeignKey("administrador.Curso", verbose_name=("Curso"), blank=True, null=True,on_delete=models.SET_NULL)
    disciplina_relacao = models.ManyToManyField("administrador.Disciplina", verbose_name=("Disciplina"), blank=True)
    
    is_staff = models.BooleanField('Membro da equipe', default=True)

    USERNAME_FIELD = 'matricula'
    REQUIRED_FIELDS = ['username' , 'email' ,'cpf', 'phone']

    def __str__(self):
        return self.username

    objects = UserManager()
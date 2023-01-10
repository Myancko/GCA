from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.

def home_view (request):
    total_usuarios =  User.objects.count()
    context = {
        "users": total_usuarios,
    }

    return render(request, 'home.html',  context)

def sign_up_student_view (request):

    return render(request, 'sign_up_student.html',  {})

def sign_up_teacher_view (request):

    return render(request, 'sign_up_teacher.html',  {})


def sign_up_course_view (request):

    return render(request, 'sign_up_course.html',  {})

def sign_up_subject_view (request):

    return render(request, 'sign_up_disciplina.html',  {})

def register_coordinator_view (request):

    return render(request, 'register.coordinator.html',  {})

def cadastro(request):
    if request.method == 'POST':
         form = ContactForm(request.POST)
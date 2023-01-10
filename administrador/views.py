from django.shortcuts import render

# Create your views here.

def home_view (request):

    return render(request, 'home.html',  {})

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
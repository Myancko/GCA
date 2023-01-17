from django.shortcuts import render

# Create your views here.

def home_professor (request):
    
    return render(request, 'home_professor.html', {})
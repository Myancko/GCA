from django.urls import path
from .views import home_professor
urlpatterns = [
    path('home_coordenador/', home_professor, name='sweet-home_teacher'),
]
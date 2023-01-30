from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('cadastro/', views.SignUpView.as_view(), name='cadastro'),
    path('alterar_senha/', views.password_change.as_view(), name='alterar_senha'),
    #path('alterar_senha/', auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'), name='cadastro'),
]
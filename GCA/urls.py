from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrador.urls')),
    path('Aluno/', include('Aluno.urls')),
    path('Coordenador/', include('coordenador.urls')),
    path('user/', include('Users.urls')),
    path('user/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

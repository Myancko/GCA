from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('administrador.urls')),
    path('user/', include('Users.urls')),
    path('user/', include('django.contrib.auth.urls')),
]

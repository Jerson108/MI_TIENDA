# productos/urls.py

from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.lista_productos, name='lista_productos'),
     path('login/', auth_views.LoginView.as_view(template_name='productos/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('crear/', views.crear_producto, name='crear_producto'),
    path('editar-producto/', views.editar_producto, name='editar_producto'),
    path('eliminar/', views.eliminar_producto, name='eliminar_producto'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
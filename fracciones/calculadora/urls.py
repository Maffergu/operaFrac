from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name='index'),
    path('proceso', views.proceso, name='proceso'),
    path('multiplicacion', views.multiplicacion, name='multiplicacion'),
    path('suma', views.suma, name='suma'),
    path('resta', views.resta, name='resta'),
    path('division', views.division, name='division'),
    path('usuarios', views.usuarios, name = 'usuarios'),
    path('usuarios_p', views.usuarios_p, name = 'usuarios_p'),
    path('usuarios_d', views.usuarios_d, name = 'usuarios_d'),
]
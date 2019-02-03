from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.index, name='index'),
    path('curso1/', views.curso1, name='curos1'),
    path('curso2/', views.curso2, name='curos2'),
    path('usr/', views.usr, name='usr'),
    path('login/', views.login, name='login'),
    path('table/', views.table, name='table'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('calendario/', views.calendario, name='calendario'),
    path('contatoProfessores/', views.contatoProfessores, name='contatoProfessores'),
    path('professor/', views.professor, name='professor'),
]

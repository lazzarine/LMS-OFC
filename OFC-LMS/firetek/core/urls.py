from django.conf.urls import url
from . import views

urlpatterns = [
    
    url (r'^$', views.index, name='index'),
    url (r'^curso1/', views.curso1, name='curso1'),
    url (r'^curso2/', views.curso2, name='curso2'),
    url (r'^usr/', views.usr, name='usr'),
    url (r'^login/', views.login, name='login'),
    url (r'^table/', views.table, name='table'),
    url (r'^cadastro/', views.cadastro, name='cadastro'),
    url (r'^calendar/', views.calendar, name='calendario'),
   
]

from django.conf.urls import url
from . import views

urlpatterns = [
    
   url (r'^$', views.index, name='index'),
   url (r'^curso1/', views.curso1, name='curso1'),
   url (r'^curso2/', views.curso2, name='curso2'),
   
]

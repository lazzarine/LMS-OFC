from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from core.views import * 

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^core/', include('core.urls')),
   url(r'^curso1/', include('core.urls')),
   url(r'^curso2/', include('core.urls')),
    
]

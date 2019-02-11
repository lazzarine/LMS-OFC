from django.contrib import admin
from django.conf.urls import include, url
from django.urls import path
from core.views import * 
from accounts.views import * 

urlpatterns = [
  path('admin/', admin.site.urls),
  path('core/', include('core.urls')),
  path('accounts/', include('accounts.urls')),
]

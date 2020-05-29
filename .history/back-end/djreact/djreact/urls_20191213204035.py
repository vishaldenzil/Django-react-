from django.contrib import admin
from django.urls import path ,include
from articles.api import urls

urlpatterns = [
    path('^api-auth/', include('rest_framework.urls')),
    path(r'^rest-auth/', include('rest_auth.urls'))
    path('admin/', admin.site.urls),
    path('api/',include(urls)),
   
    
]

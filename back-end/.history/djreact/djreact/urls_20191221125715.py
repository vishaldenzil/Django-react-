from django.contrib import admin
from django.urls import path ,include
from articles.api.urls import 

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('admin/', admin.site.urls),
    path('api/',include(urls)),
   
    
]

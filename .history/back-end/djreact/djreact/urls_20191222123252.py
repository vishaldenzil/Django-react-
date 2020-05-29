from django.contrib import admin
from django.urls import path ,include

urlpatterns = [
    path(r'^api-auth/', include('rest_framework.urls')),
    path(r'^rest-auth/', include('rest_auth.urls')),
    path(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    path(r'^admin/', admin.site.urls),
    path(r'^api/article/',include('articles.api.urls')),
    path(r'^api/users/',include('users.urls')),
]

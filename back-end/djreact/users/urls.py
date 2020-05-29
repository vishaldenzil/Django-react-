from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView ,OrganisationUserLoginView
from django.urls import path
router = DefaultRouter(trailing_slash=False)

router.register(r'register', UserRegistrationView, basename='user_register')
router.register(r'login', OrganisationUserLoginView, basename='org_user_login')

urlpatterns = [    
    *router.urls
]


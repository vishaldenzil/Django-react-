from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView
from django.urls import path

# router = DefaultRouter()
# router.register(r'register', UserRegistrationView, basename='user_register')

# urlpatterns = router.urls

urlpatterns = [
    path(r'^myapp1/','register', UserRegistrationView.as_view(),
         name="org_user_registration")
]
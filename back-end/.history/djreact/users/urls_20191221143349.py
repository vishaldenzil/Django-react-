from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView

# router = DefaultRouter()
# router.register(r'register', UserRegistrationView, basename='user_register')

# urlpatterns = router.urls


urlpatterns = [
    path("org_users/register", OrganisationUserRegistrationView.as_view(),
         name="org_user_registration")




]
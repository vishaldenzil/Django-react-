from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'register', UserRegistrationView, basename='user_register')

urlpatterns = router.urls


urlpatterns = [
    path("org_users/register", OrganisationUserRegistrationView.as_view(),
         name="org_user_registration"),
    path("org_users/reset_password/<uidb64>/<token>",
         OrganisationUserResetPasswordView.as_view(), name="org_user_reset_password"),
    path('org_users/send_reset_password_link', OrganisationUserSendResetPasswordLinkView.as_view(),
         name='org_user_send_reset_password_link'),
    path('org_users/change_password', OrganisationUserChangePasswordView.as_view(),
         name='org_user_change_password'),
    path('org_users/login', OrganisationUserLoginView.as_view(),
         name='org_user_login'),
    path('external_users/otp', ExternalUserOTP.as_view(),
         name='external_users_otp'),
    path('external_users/login', ExternalUserLogin.as_view(),
         name='external_users_login'),





   
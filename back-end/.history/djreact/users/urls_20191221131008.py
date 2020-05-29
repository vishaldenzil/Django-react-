from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'', UserRegistrationView, basename='articles')
urlpatterns = router.urls
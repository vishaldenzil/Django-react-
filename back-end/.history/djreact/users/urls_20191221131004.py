from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'', UserRegistrationV, basename='articles')
urlpatterns = router.urls
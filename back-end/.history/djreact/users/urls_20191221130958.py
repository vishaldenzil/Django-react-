from rest_framework.routers import DefaultRouter
from .views import UserRegistrationView

router = DefaultRouter()
router.register(r'', UserRegistrationViewleViewSet, basename='articles')
urlpatterns = router.urls
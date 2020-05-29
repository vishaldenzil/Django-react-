from rest_framework.routers import DefaultRouter
from .views import 

router = DefaultRouter()
router.register(r'', ArticleViewSet, basename='articles')
urlpatterns = router.urls
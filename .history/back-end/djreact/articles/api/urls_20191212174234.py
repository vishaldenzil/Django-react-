from rest_framework.routers import DefaultRouter
from .views import ArticleListView




router = DefaultRouter()
router.register(r'', ArticleListView, basename='articles')
urlpatterns = router.urls
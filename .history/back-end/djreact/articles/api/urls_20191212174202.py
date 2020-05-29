from django.urls import path

from .views import ArticleListView


urlpatterns = [
  path('',ArticleListView.as_view()),
  path('create/',ArticleCreateView.as_view()),
  path('<pk>',ArticleDetailView.as_view())

]


from myapp.views import UserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ArticleListView, basename='artcole')
urlpatterns = router.urls
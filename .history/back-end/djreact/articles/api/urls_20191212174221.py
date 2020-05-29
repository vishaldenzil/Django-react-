from django.urls import path

from .views import ArticleListView


urlpatterns = [
  path('',ArticleListView.as_view()),
  path('create/',ArticleCreateView.as_view()),
  path('<pk>',ArticleDetailView.as_view())

]





router = DefaultRouter()
router.register(r'', ArticleListView, basename='articles')
urlpatterns = router.urls
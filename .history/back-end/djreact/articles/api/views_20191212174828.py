# from rest_framework.generics import ListAPIView, RetrieveAPIView,CreateAPIView
from rest_framework import viewsets
from articles.models import Article
from .serializers import ArticleSerializer


class ArticleView(viewsets.ViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
from django.shortcuts import render
from rest_framework import viewsets




class ArticleViewSet(viewsets.ModelViewSet):
    pass


# class ArticleDetailView(RetrieveAPIView):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


# class ArticleCreateView(CreateAPIView):
#     queryset = Article.objects.all()
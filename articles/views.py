from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404
from articles import serializers
from articles.models import Article
from articles.serializers import ArticlesSerializers
from drf_yasg.utils import swagger_auto_schema

# Create your views here.
"""
#함수형 view

@api_view(['GET', 'POST'])
def ArticleList(request):
    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticlesSerializers(articles, many=True)
        
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ArticlesSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET', 'PUT', 'DELETE'])
def articleDetail(request, article_id):
    if request.method == 'GET':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticlesSerializers(article)
        return Response(serializer.data)
    elif request.method == 'PUT':
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticlesSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
    elif request.method =='DELETE':
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        """
        
#class형 view
class ArticleList(APIView):
    def get(self, request, format=None):
        articles = Article.objects.all()
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)
    
    @swagger_auto_schema(request_body=ArticlesSerializers)
    def post(self, request, format=None):
        serializer = ArticlesSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
class articleDetail(APIView):
    def get(self, request, article_id, format=None):
        articles = Article.objects.all()
        serializer = ArticlesSerializers(articles, many=True)
        return Response(serializer.data)
    
    def put(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        serializer = ArticlesSerializers(article, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, article_id, format=None):
        article = get_object_or_404(Article, id=article_id)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


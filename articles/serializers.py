from rest_framework import serializers
from articles.models import Article

class ArticlesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"
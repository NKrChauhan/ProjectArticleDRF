from rest_framework import serializers


class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    banner = serializers.ImageField(required=False)
    content = serializers.CharField(max_length=200)

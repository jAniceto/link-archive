from rest_framework.serializers import ModelSerializer
from .models import Link, Tag


class LinkSerializer(ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'


class TagSerializer(ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'
from rest_framework.serializers import ModelSerializer

from .models import Country, Category


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
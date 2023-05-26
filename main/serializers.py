from rest_framework.serializers import ModelSerializer

from .models import Country, Category, Tiket
from review.serializers import CommentSerializer


class CountrySerializer(ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['rating'] = instance.average_rating
        rep['comments'] = CommentSerializer(instance.comments.all(), many=True, context=self.context).data
        return rep 


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TiketSerializer(ModelSerializer):
    class Meta:
        model = Tiket
        fields = '__all__'
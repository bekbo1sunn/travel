from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.parsers import MultiPartParser

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from .models import Country, Category, Tiket, CategoryTikets
from .serializers import CountrySerializer, CategorySerializer, TiketSerializer, CategoryTiketsSerializer


class CountryViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    parser_classes = [MultiPartParser]
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('title',)
    search_fields = ('title', 'description')


class CountryListCreateAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    parser_classes = [MultiPartParser]



class CategoryViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]


class CategoryListCreateAPIView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer



class TiketViewSet(mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [IsAuthenticated, IsAdminUser]
    filter_backends = (SearchFilter, DjangoFilterBackend)
    filterset_fields = ('flight_name', 'category')
    search_fields = ('category','arrival')
    

class TiketListAPIView(ListAPIView):
    queryset = Tiket.objects.all()
    serializer_class = TiketSerializer
    


class CategoryTiketsViewSet(mixins.CreateModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    
    queryset = CategoryTikets.objects.all()
    serializer_class = CategoryTiketsSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

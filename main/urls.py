from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CategoryViewSet, TiketViewSet, CategoryListCreateAPIView, CountryListCreateAPIView, TiketListAPIView, CategoryTiketsViewSet


router = DefaultRouter()
router.register("countrys", CountryViewSet)
router.register("category", CategoryViewSet)
router.register("tikets", TiketViewSet)
router.register("category_tikets", CategoryTiketsViewSet)



urlpatterns = [
    path("", include(router.urls)),
    path("category/list/", CategoryListCreateAPIView.as_view()),
    path("countrys/list/", CountryListCreateAPIView.as_view()),
    path("tiket/list/", TiketListAPIView.as_view()),
]
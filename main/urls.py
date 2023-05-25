from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CountryViewSet, CategoryViewSet


router = DefaultRouter()
router.register("countrys", CountryViewSet)
router.register("category", CategoryViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
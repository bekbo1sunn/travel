from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.routers import DefaultRouter

from .views import RegisterUserView, TopUpBillingView, ProfileViewSet, LogoutAPIView


router = DefaultRouter()
router.register("profile", ProfileViewSet)

urlpatterns = [
    path('register/', RegisterUserView.as_view()),
    path('token/', TokenObtainPairView.as_view()),
    path('billing/top-up/', TopUpBillingView.as_view()),
    path('', include(router.urls)),
    path('logout/', LogoutAPIView.as_view()),
    
]
from decimal import Decimal, InvalidOperation
from django.shortcuts import get_object_or_404, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken
from decouple import config

from .serializers import RegisterUserSerializer, BillingSerializer, ProfileSerializer, LogoutSerializer
from .models import User


class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer())
    def post(self, request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Вы успешно зарегестрировались", status=201)


class ActivateView(APIView):
    def get(self, request, activation_code):
        user = get_object_or_404(User, activation_code=activation_code)
        user.is_active = True
        user.activation_code = ''
        user.save()
        LINK = config("LINK")
        return redirect(LINK)


class TopUpBillingView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(request_body=BillingSerializer())
    def post(self, request):
        # {"amount": 100}
        amount = request.data.get("amount")
        if not amount:
            return Response("amount is required", status=400)
        try:
            amount = Decimal(amount)
        except InvalidOperation:
            return Response("invalid amount", status=400)
        billing = request.user.billing
        if billing.top_up(amount):
            return Response(status=200)
        return Response("invalid amount", status=400)


class ProfileViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = ProfileSerializer



class LogoutAPIView(APIView):
    '''
    Only authorized users can make a logout
    '''
    permission_classes = (IsAuthenticated,)
    serializer_class = [LogoutSerializer,]
    @swagger_auto_schema(request_body=LogoutSerializer)
    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=204)
        except Exception as e:
            return Response(status=400)
from rest_auth.models import TokenModel

from rest_framework import status
from rest_framework.generics import CreateAPIView, GenericAPIView
from rest_framework.response import Response

from users.serializers import ProfileRegisterSerializer, ProfileLoginSerializer, StuffRegisterSerializer, StuffLoginSerializer ,CourierRegisterSerializer, CourierLoginSerializer

from django.contrib.auth import authenticate


class ProfileRegisterView(CreateAPIView):
    serializer_class = ProfileRegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)   #вызывает serializers.save()
        return Response('success', status=status.HTTP_201_CREATED)


class ProfileLoginView(GenericAPIView):
    serializer_class = ProfileLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        username = serializer.data.get('username')
        password = serializer.data.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            token = TokenModel.objects.get(user=user)
            return Response({'key': token.key}, status=status.HTTP_201_CREATED)
        return Response('invalid login', status=status.HTTP_401_UNAUTHORIZED)


class StuffRegisterView(ProfileRegisterView):
    serializer_class = StuffRegisterSerializer


class StuffLoginView(ProfileLoginView):
    serializer_class = StuffLoginSerializer


class CourierRegisterView(ProfileRegisterView):
    serializer_class = CourierRegisterSerializer


class CourierLoginView(ProfileLoginView):
    serializer_class = CourierLoginSerializer
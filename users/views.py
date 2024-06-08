from django.contrib.auth import authenticate
from rest_framework import generics, status, viewsets
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Character
from .permissions import IsCharacterOwner
from .serializers import UserRegisterSerializer, CharacterSerializer


class UserRegisterView(generics.CreateAPIView):
    """Users registeration."""

    permission_classes = [AllowAny]
    serializer_class = UserRegisterSerializer

    def post(self, request):
        data = request.data
        srz_data = self.serializer_class(data=data)
        srz_data.is_valid(raise_exception=True)
        user = srz_data.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {"message": "user registered", "token": token.key},
            status=status.HTTP_201_CREATED,
        )


class UserLoginView(APIView):
    """Users Login page."""

    def post(self, request):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user = authenticate(request, username=username, password=password)
        if not user:
            return Response(
                "username or password is incorrect.",
                status=status.HTTP_404_NOT_FOUND,
            )
        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {
                "type": "redirect",
                "url": "users:home_page",
                "data": {"token": token.key},
            },
            status=status.HTTP_200_OK,
        )


class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
    # lookup_field = "name"

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsCharacterOwner]
        return [permission() for permission in permission_classes]


class MyCharactersListView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.filter(owner=self.request.user)

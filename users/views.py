from rest_framework import generics
from rest_framework.permissions import AllowAny

from users.models import User
from users.serializator import UserSerializer


class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()  # queryset обязательный - Это набор запросов, в отношении которого должна обеспечиваться уникальность.
    serializer_class = UserSerializer
    # permission_classes = [AllowAny]


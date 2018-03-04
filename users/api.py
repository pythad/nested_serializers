from rest_framework import generics

from .models import MyUser
from .serializers import MyUserSerializer


class MyUserList(generics.ListCreateAPIView):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

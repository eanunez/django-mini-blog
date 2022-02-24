from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authentication import BasicAuthentication
from .serializers import CustomTokenObtainPairSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
# from django.contrib.auth.models import User
from post.models import User
from .serializers import RegisterSerializer
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response


class EmailTokenObtainPairView(TokenObtainPairView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        resp = {"message": "Signup Successful!", "data": serializer.data}
        return Response(resp, status=status.HTTP_201_CREATED, headers=headers)

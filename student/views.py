
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


class CustomAuthentication(BaseAuthentication):

    def get_raw_token(self, header):
        parts = header.split()

        if len(parts) == 0:
            raise AuthenticationFailed(
                ("Authorization header can't be empty"),
                code="bad_authorization_header",
            )

        if len(parts) != 2:
            raise AuthenticationFailed(
                ("Authorization header must contain two space-delimited "
                  "values"),
                code="bad_authorization_header",
            )

        return parts[1]

    def authenticate(self, request):
        header = request.META.get("HTTP_AUTHORIZATION")

        if header is None:
            raise AuthenticationFailed("please you must provide token")

        raw_token = self.get_raw_token(header)
        if raw_token is None:
            raise AuthenticationFailed("please you must provide token")
        token = Token.objects.filter(key=raw_token).first()

        if token is None:
            raise AuthenticationFailed("invalid token")

        return token.user, token.key


class StudentViewSet(viewsets.ModelViewSet):
    # authentication_classes = [CustomAuthentication]
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]



class UserLoginView(generics.CreateAPIView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)

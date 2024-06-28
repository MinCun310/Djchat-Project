from django.conf import settings
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from account.models import Account
from account.schemas import user_list_docs
from account.serializers import AccountSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer, RegisterSerializer


# Create your views here.

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        response = Response("Log out successfully")
        response.delete_cookie(settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"])
        response.delete_cookie(settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"])
        return response


class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            forbidden_username = ['admin', 'root', 'superuser']
            if username in forbidden_username:
                return Response({'error': 'Username is not allowed'}, status=status.HTTP_409_CONFLICT)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        errors = serializer.errors
        if 'username' in errors and 'non_field_errors' not in errors:
            return Response({'error': 'Username already exists'}, status=status.HTTP_409_CONFLICT)
        return Response(errors, status=status.HTTP_400_BAD_REQUEST)


class AccountView(APIView):
    permission_classes = [IsAuthenticated]

    @user_list_docs
    def get(self, request):
        queryset = Account.objects.all()
        params_user_id = request.query_params.get("userId")
        try:
            if params_user_id:
                queryset_user = queryset.filter(pk=params_user_id)
                if queryset_user.exists():
                    serializer = AccountSerializer(instance=queryset_user, many=True)
                    return Response(serializer.data)
                else:
                    return Response([])
        except ValueError:
            raise ValidationError('userId must be an integer')
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)


class JWTSetCookieMixin:
    def finalize_response(self, request, response, *args, **kwargs):
        if response.data.get('refresh'):
            response.set_cookie(
                settings.SIMPLE_JWT["REFRESH_TOKEN_NAME"],
                response.data["refresh"],
                max_age=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"],
            )
        if response.data.get('access'):
            response.set_cookie(
                settings.SIMPLE_JWT["ACCESS_TOKEN_NAME"],
                response.data["access"],
                max_age=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"],
                httponly=True,
                samesite=settings.SIMPLE_JWT["JWT_COOKIE_SAMESITE"],
            )
            # Xóa access token để đảm bảo token chỉ tồn tai trong cookie
            del response.data["access"]

        # user_id = response.data['user_id']
        # print('user_id: ', user_id)

        return super().finalize_response(request, response, *args, **kwargs)


class JWTCookieTokenObtainPairView(JWTSetCookieMixin, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class JWTCookieTokenRefreshView(JWTSetCookieMixin, TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer

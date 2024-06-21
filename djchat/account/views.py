from django.conf import settings
from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

from account.models import Account
from account.schemas import user_list_docs
from account.serializers import AccountSerializer, CustomTokenObtainPairSerializer


# Create your views here.


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

        user_id = response.data['user_id']
        print('user_id: ', user_id)

        # del response.data["access"]

        return super().finalize_response(request, response, *args, **kwargs)


class JWTCookieTokenObtainPairView(JWTSetCookieMixin, TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

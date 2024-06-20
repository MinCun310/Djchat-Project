from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from account.models import Account
from account.schemas import user_list_docs
from account.serializers import AccountSerializer


# Create your views here.

class AccountView(APIView):
    permission_classes = [IsAuthenticated]

    @user_list_docs
    def get(self, request):
        queryset = Account.objects.all()
        print('queryset', queryset)
        params_user_id = request.query_params.get("userId")
        print("==>",params_user_id)
        try:
            if params_user_id:
                queryset_user = queryset.filter(pk=params_user_id)
                if queryset_user.exists():
                    serializer = AccountSerializer(instance=queryset_user, many=True)
                    return Response(serializer.data)
                else:
                    return Response({})
        except ValueError:
            raise ValidationError('userId must be an integer')
        serializer = AccountSerializer(queryset, many=True)
        return Response(serializer.data)

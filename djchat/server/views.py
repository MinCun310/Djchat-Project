from django.shortcuts import render
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.db.models import Count

from .models import Server, Category

from .serializers import ServerSerializer, CategorySerializer

from .mixins import CustomPermissionMixin

from .schemas import server_list_docs

from drf_spectacular.utils import extend_schema


# Create your views here.

class CategoryView(APIView):
    @extend_schema(responses=CategorySerializer)
    def get(self, request):
        query_category = Category.objects.all()
        serializer = CategorySerializer(instance=query_category, many=True)
        return Response(serializer.data)


class ServerView(APIView):
    @server_list_docs
    def get(self, request):
        """
            Fetches servers based on various query parameters provided in the request.

            This function allows fetching servers from the database based on the following query parameters:
            - `category`: Filters servers by category name.
            - `server_id`: Filters servers by category ID.
            - `user`: Filters servers by username.
            - `quantity`: Limits the number of servers fetched.
            - `num_members`: Annotates servers with the number of members if set to 'true'.

            Parameters:
            request (HttpRequest): The HTTP request object containing query parameters.

            Returns:
            Response: A Response object containing serialized server data and a message indicating the result of the operation.
        """

        query_server = Server.objects.all()
        param_category = request.query_params.get('category')
        param_user = request.query_params.get('user')
        param_serverId = request.query_params.get('server_id')
        param_quantity = request.query_params.get('quantity')
        with_num_members = request.query_params.get('num_members') == 'true'
        if param_category:
            query_category_server = query_server.filter(category__name=param_category)
            if query_category_server.exists():
                serializer = ServerSerializer(instance=query_category_server, many=True)
                return Response(serializer.data)
                # return Response({
                #     'data': serializer.data,
                #     'message': 'Server is fetched successfully by category'
                # })
            else:
                return Response({
                    'message': f'Server with category {param_category} does not exist'
                })
        elif param_serverId:
            # if not request.user.is_authenticated:
            #     raise AuthenticationFailed('User is not authenticated')
            try:
                query_serverId = query_server.filter(id=param_serverId)
                if query_serverId.exists():
                    serializer = ServerSerializer(instance=query_serverId, many=True)
                    return Response(serializer.data)
                    # return Response({
                    #     'data': serializer.data,
                    #     'message': 'Server is fetched successfully by id'
                    # })
                else:
                    return Response({
                        'message': f'Server with id {param_serverId} does not exist'
                    })
            except ValueError:
                raise ValidationError('categoryId must be an integer')
        elif param_user:
            # request.user.is_authenticated: check to user have logged in
            if request.user.is_authenticated:
                query_user_server = query_server.filter(member__username=param_user)
                print('check is_authenticated: ', request.user.is_authenticated)
                if query_user_server.exists():
                    serializer = ServerSerializer(instance=query_user_server, many=True)
                    return Resposne(serializer.data)
                    # return Response({
                    #     'data': serializer.data,
                    #     'message': 'Server is fetched successfully by user'
                    # })
                else:
                    return Response({
                        'message': f'Server with user {param_user} does not exist'
                    })
            else:
                raise AuthenticationFailed('User is not authenticated')
        elif param_quantity:
            try:
                query_quantity_server = query_server.order_by('-id')[:int(param_quantity)]
                if query_quantity_server.exists():
                    serializer = ServerSerializer(instance=query_quantity_server, many=True)
                    return Response(serializer.data)
                    # return Response({
                    #     'data': serializer.data,
                    #     'message': 'Server is fetched successfully by quantity'
                    # })
            except ValueError:
                raise ValidationError('quantity must be an integer')
        elif with_num_members:
            query_server = query_server.annotate(num_members=Count('member'))
            serializer = ServerSerializer(instance=query_server, many=True, context={'num_members': True})
            return Response(serializer.data)
            # return Response({
            #     'data': serializer.data,
            #     'message': 'All servers are fetched successfully with num_members = true'
            # })
        else:
            serializer = ServerSerializer(instance=query_server, many=True)
            # return Response({
            #     'data': serializer.data,
            #     'message': 'All servers are fetched successfully'
            # })
            return Response(serializer.data)

from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema

from .serializers import ServerSerializer

server_list_docs = extend_schema(
    responses=ServerSerializer(many=True),
    parameters=[
        OpenApiParameter(
            name='category',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Filter servers by category name'
        ),
        OpenApiParameter(
            name='server_id',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter servers by id'
        ),
        OpenApiParameter(
            name='user',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='Filter servers by user name'
        ),
        OpenApiParameter(
            name='quantity',
            type=OpenApiTypes.INT,
            location=OpenApiParameter.QUERY,
            description='Filter servers by quantity'
        ),
        OpenApiParameter(
            name='num_members',
            type=OpenApiTypes.BOOL,
            location=OpenApiParameter.QUERY,
            description='Get all servers with num_members = true'
        ),
    ],
)

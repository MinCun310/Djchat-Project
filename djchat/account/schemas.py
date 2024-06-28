from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import extend_schema, OpenApiParameter

from account.serializers import AccountSerializer

user_list_docs = extend_schema(
    responses=AccountSerializer(),
    parameters=[
        OpenApiParameter(
            name='user_id',
            type=OpenApiTypes.STR,
            location=OpenApiParameter.QUERY,
            description='User ID',
        ),
    ],
)

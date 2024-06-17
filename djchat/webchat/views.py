from rest_framework.views import APIView
from rest_framework.response import Response

from webchat.models import Conversation
from webchat.schemas import message_list_docs
from webchat.serializers import MessageSerializer


# Create your views here.

class MessageView(APIView):
    @message_list_docs
    def get(self, request):
        try:
            param_channel_id = request.query_params.get('channel_id')
            conversation = Conversation.objects.get(channel_id=param_channel_id)
            messages = conversation.conversation_message.all()
            serializer = MessageSerializer(instance=messages, many=True)
            return Response(serializer.data)
        except Conversation.DoesNotExist:
            return Response([])

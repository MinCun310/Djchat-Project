from rest_framework import serializers

from .models import Server, Category, Channel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ChannelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Channel
        fields = '__all__'


class ServerSerializer(serializers.ModelSerializer):
    channel_server = ChannelSerializer(many=True)
    num_members = serializers.SerializerMethodField()
    category = serializers.StringRelatedField() # hiện tên category trên frontend thay vì hiện id

    class Meta:
        model = Server
        fields = ['id', 'name', 'owner', 'category', 'description', 'member', 'channel_server', 'num_members', 'icon', 'banner']

    def get_num_members(self, obj):
        if hasattr(obj, 'num_members'):
            return obj.num_members
        return None
        # return obj.member.count()

    def to_representation(self, instance):
        data = super().to_representation(instance)
        num_members = self.context.get('num_members')
        if not num_members:
            data.pop('num_members', None)
        return data

from rest_framework import serializers

from apps.goods.models import GoodsChannel, GoodsChannelGroup


class GoodsChannelSerializer(serializers.ModelSerializer):
    group_id=serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()
    group=serializers.StringRelatedField(read_only=True)
    class Meta:
        model = GoodsChannel
        fields = '__all__'


class GoodsChannelGroupSelizer(serializers.ModelSerializer):
    name=serializers.StringRelatedField()
    class Meta:
        model = GoodsChannelGroup
        fields = '__all__'





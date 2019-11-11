from rest_framework import serializers

from apps.goods.models import GoodsChannel


class GoodsChannelSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoodsChannel
        fields = '__all__'

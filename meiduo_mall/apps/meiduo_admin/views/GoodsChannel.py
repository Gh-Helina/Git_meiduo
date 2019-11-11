from rest_framework.viewsets import ModelViewSet

from apps.goods.models import GoodsChannel
from apps.meiduo_admin.serializers.GoodsChannelSerializer import GoodsChannelSerializer
from apps.meiduo_admin.utils import PageNum


class GoodsChannelView(ModelViewSet):
    serializer_class = GoodsChannelSerializer
    queryset = GoodsChannel.objects.all()
    pagination_class = PageNum
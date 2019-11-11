from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import GoodsChannel, GoodsCategory,GoodsChannelGroup
from apps.meiduo_admin.serializers.GoodsChannelSerializer import GoodsChannelSerializer,GoodsChannelGroupSelizer
from apps.meiduo_admin.serializers.SpuSerializer import CategorysSerizliser
from apps.meiduo_admin.utils import PageNum


class GoodsChannelView(ModelViewSet):
    serializer_class = GoodsChannelSerializer
    queryset = GoodsChannel.objects.all()
    pagination_class = PageNum

    def channel(self, request):
        # 1、获取一级分类数据
        data = GoodsCategory.objects.filter(parent=None)
        # 2、序列化返回分类数据
        ser = CategorysSerizliser(data, many=True)
        return Response(ser.data)

    def goodschannelgroup(self,request):
        # 1、查询所有组数据
        data = GoodsChannelGroup.objects.all()
        # 2、序列化返回组数据
        ser = GoodsChannelGroupSelizer(data, many=True)
        return Response(ser.data)

from fdfs_client.client import Fdfs_client
from rest_framework import request
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKUImage, SKU
from apps.meiduo_admin.serializers.ImageSerializer import ImageSeriazlier, SKUSeriazlier
from apps.meiduo_admin.utils import PageNum


class ImageView(ModelViewSet):
    # 图片序列化器
    serializer_class = ImageSeriazlier
    # 图片查询集
    queryset = SKUImage.objects.all()
    # 分页
    pagination_class = PageNum

    def simple(self, request):
        # 查询sku表
        data = SKU.objects.all()
        # 返回sku表
        ser = SKUSeriazlier(data, many=True)
        return Response(ser.data)


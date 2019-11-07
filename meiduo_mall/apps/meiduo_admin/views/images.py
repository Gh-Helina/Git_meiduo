from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SKUImage
from apps.meiduo_admin.serializers.ImageSerializer import ImageSeriazlier
from apps.meiduo_admin.utils import PageNum


class ImageView(ModelViewSet):
    # 图片序列化器
    serializer_class = ImageSeriazlier
    # 图片查询集
    queryset = SKUImage.objects.all()
    # 分页
    pagination_class = PageNum
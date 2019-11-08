from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.goods.models import SKU, GoodsCategory
from apps.meiduo_admin.serializers.SkuSerializer import SKUSerializer, GoodsCategoryserializer
from apps.meiduo_admin.utils import PageNum


class SKUGoodsView(ModelViewSet):
    # 指定序列化器
    serializer_class = SKUSerializer
    # 指定查询集
    queryset = SKU.objects.all()
    # 指定分页器 进行分页返回
    pagination_class = PageNum

    # 重写get_queryset
    ######搜索##########
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword is '' or keyword is None:
            return SKU.objects.filter()
        else:
            return SKU.objects.filter(name__contains=keyword)

    ########三级分类方法###########
    def catrgoties(self, request):

        # 1.查询分类表获取三级分类
        data = GoodsCategory.objects.filter(subs=None)
        # 2.返回三级分类
        ser = GoodsCategoryserializer(data, many=True)
        return Response(ser.data)

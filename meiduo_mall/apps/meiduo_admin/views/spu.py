from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPU, Brand, GoodsCategory
from apps.meiduo_admin.serializers.SpecSerializer import SPUSerializer
from apps.meiduo_admin.serializers.SpuSerializer import SPUBrandsSerizliser, CategorysSerizliser
from apps.meiduo_admin.utils import PageNum


class SPUGoodsView(ModelViewSet):
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    pagination_class = PageNum


 # 在类中跟定义获取品牌数据的方法
    def simple(self, request):
        # 1、查询所有品牌数据
        data = Brand.objects.all()
        # 2、序列化返回品牌数据
        ser = SPUBrandsSerizliser(data, many=True)

        return Response(ser.data)

    def channel(self, request):
        # 1、获取一级分类数据
        data = GoodsCategory.objects.filter(parent=None)
        # 2、序列化返回分类数据
        ser = CategorysSerizliser(data, many=True)
        return Response(ser.data)

    def channels(self, request, pk):
        # 1、获取二级和三级分类数据
        data = GoodsCategory.objects.filter(parent_id=pk)
        # 2、序列化返回分类数据
        ser = CategorysSerizliser(data, many=True)
        return Response(ser.data)
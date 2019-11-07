from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.goods.models import SPUSpecification, SpecificationOption, SKUSpecification
from apps.meiduo_admin.serializers.OptionsSerializer import SpecificationOptionSerializer
from apps.meiduo_admin.serializers.SpecSerializer import SPUSpecificationSerializer
from apps.meiduo_admin.utils import PageNum


class OptionView(ModelViewSet):
    # 指定序列化器
    serializer_class = SpecificationOptionSerializer
    # 指定字符集
    queryset = SpecificationOption.objects.all()
    # 指定分页器

    pagination_class = PageNum

    # 自定义获取spu商品数据
    def simple(self, request):
        # 1.查询所有spu表数据
        data = SPUSpecification.objects.all()
        # 2.进行序列化返回
        ser = SPUSpecificationSerializer(data, many=True)
        return Response(ser.data)
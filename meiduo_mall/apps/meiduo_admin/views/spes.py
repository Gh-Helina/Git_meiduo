from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import DjangoModelPermissions
from apps.goods.models import SPUSpecification, SPU
from apps.meiduo_admin.serializers.SpecSerializer import SPUSpecificationSerializer, SPUSerializer

from apps.meiduo_admin.utils import PageNum


class SpecsView(ModelViewSet):
    # 指定序列化器
    serializer_class = SPUSpecificationSerializer
    # 指定字符集
    queryset = SPUSpecification.objects.all()
    # 指定分页器
    pagination_class = PageNum
    permission_classes = [DjangoModelPermissions]

 #自定义获取spu商品数据
    def simple(self,request):
        # 1.查询所有spu表数据
        spu=SPU.objects.all()
        # 2.进行序列化返回
        ser=SPUSerializer(spu,many=True)
        return Response (ser.data)

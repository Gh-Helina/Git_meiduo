from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.goods.models import SPU, Brand, GoodsCategory
from apps.meiduo_admin.serializers.SpuSerializer import SPUSerializer
from apps.meiduo_admin.serializers.SpuSerializer import SPUBrandsSerizliser, CategorysSerizliser
from apps.meiduo_admin.utils import PageNum


class SPUGoodsView(ModelViewSet):
    serializer_class = SPUSerializer
    queryset = SPU.objects.all()
    pagination_class = PageNum


    # 在类中跟定义获取品牌数据的方法
    def brands(self, request):
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

    def image(self,request):
        # 1.获取图片数据
        # 不能直接读取data信息
        image = request.data.get('image')
        # 2、链接fasfDFS
        client = Fdfs_client('/home/python/Desktop/Git_meiduo/meiduo_mall/utils/fastdfs/client.conf')
        # 3、上传图片
        res = client.upload_by_buffer(image.read())
        # 4、判断是否成功
        if res['Status'] != 'Upload successed.':
            return Response({'error': '上传失败'}, status=400)
        # 5、提取图片链接地址
        path = res.get('Remote file_id')
        # 6.构建路径
        image_url = 'http://image.meiduo.site:8888/' + path
        # 7.返回给前端
        # img_url前端的字段
        return Response({'img_url': image_url})

# class SKUGoodsView(ModelViewSet):
#
#     serializer_class =SKUGoodsSerializer
#     pagination_class = PageNum
#
#     def get_queryset(self):
#         keyword=self.request.query_params.get('keyword')
#         if keyword == '' or keyword is None:
#             return SKU.objects.all()
#
#         else:
#             return SKU.objects.filter(name=keyword)
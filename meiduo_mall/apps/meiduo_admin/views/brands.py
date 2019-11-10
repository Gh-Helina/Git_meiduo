from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.goods.models import Brand
from apps.meiduo_admin.serializers.BrandsSerializer import BrandsSerializer
from apps.meiduo_admin.utils import PageNum

class BrandsView(ModelViewSet):
    serializer_class = BrandsSerializer
    queryset = Brand.objects.all()
    pagination_class = PageNum

    def image(self, request):
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
        # 进入etc/hosts文件注册域名
        image_url = 'http://image.meiduo.site:8888/' + path
        # 7.返回给前端
        # img_url前端的字段
        return Response({'img_url': image_url})
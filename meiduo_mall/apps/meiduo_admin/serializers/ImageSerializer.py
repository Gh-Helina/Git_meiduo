from rest_framework import serializers
from fdfs_client.client import Fdfs_client
from rest_framework.response import Response

from apps.goods.models import SKUImage, SKU
# from apps.goods.utils import get_detail_html
from celery_tasks.static_html.tasks import get_detail_html

class ImageSeriazlier(serializers.ModelSerializer):
    # 显示指明覆盖下面的
    # sku = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = SKUImage
        fields = '__all__'

        # 重写保存图片表业务

    def create(self, validated_data):
        # 1、获取前端sku对象
        sku = validated_data.get('sku')
        # 2、获取前端传递的图片数据
        image = validated_data['image']
        # 3、链接fasfDFS
        client = Fdfs_client('/home/python/Desktop/Git_meiduo/meiduo_mall/utils/fastdfs/client.conf')
        # 4、上传图片
        res = client.upload_by_buffer(image.read())
        # 5、判断是否成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        # 6、提取图片链接地址
        path = res.get('Remote file_id')

        # 7、保存图片表
        img = SKUImage.objects.create(sku=sku, image=path)
        # 生成静态化页面
        # get_detail_html(sku.id)
        #异步处理调用
        get_detail_html.delay(sku.id)
        return img

    def update(self, instance, validated_data):
        # 1、获取前端sku对象
        sku = validated_data.get('sku')
        # 2、获取前端传递的图片数据
        image = validated_data['image']
        # 3、链接fasfDFS
        client = Fdfs_client('/home/python/Desktop/Git_meiduo/meiduo_mall/utils/fastdfs/client.conf')
        # 4、上传图片
        res = client.upload_by_buffer(image.read())
        # 5、判断是否成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        # 6、提取图片链接地址
        path = res.get('Remote file_id')

        # 7、保存图片表
        instance.image = path
        # 更新图片
        instance.save()
        # 生成静态化页面
        # get_detail_html(sku.id)

        # 异步处理调用
        get_detail_html.delay(sku.id)
        return instance

 ###########商品序列化器########
class SKUSeriazlier(serializers.ModelSerializer):
    class Meta:
        model = SKU
        fields = '__all__'

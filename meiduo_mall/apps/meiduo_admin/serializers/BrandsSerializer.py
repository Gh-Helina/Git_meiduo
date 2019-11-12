########品牌序列化器###############
from fdfs_client.client import Fdfs_client
from rest_framework import serializers

from apps.goods.models import Brand


class BrandsSerializer(serializers.ModelSerializer):


    class Meta:
        model = Brand
        fields = '__all__'

        # 重写保存图片表业务

    def create(self, validated_data):


        # 1、获取前端brand对象
        brand = validated_data.get('name')
        first_letter = validated_data.get('first_letter')
        # 2、获取前端传递的图片数据
        logo = validated_data['logo']
        # 3、链接fasfDFS
        client = Fdfs_client('/home/python/Desktop/Git_meiduo/meiduo_mall/utils/fastdfs/client.conf')
        # 4、上传图片
        res = client.upload_by_buffer(logo.read())
        # 5、判断是否成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        # 6、提取图片链接地址
        path = res.get('Remote file_id')

        # 7、保存图片表
        log = Brand.objects.create(name=brand,first_letter=first_letter, logo=path)
        # 生成静态化页面
        # get_detail_html(sku.id)
        # 异步处理调用
        # get_detail_html.delay(sku.id)
        return log

    def update(self, instance, validated_data):
        # 1、获取前端brand对象
        brand = validated_data.get('name')
        first_letter = validated_data.get('first_letter')
        # 2、获取前端传递的图片数据
        logo = validated_data['logo']
        # 3、链接fasfDFS
        client = Fdfs_client('/home/python/Desktop/Git_meiduo/meiduo_mall/utils/fastdfs/client.conf')
        # 4、上传图片
        res = client.upload_by_buffer(logo.read())
        # 5、判断是否成功
        if res['Status'] != 'Upload successed.':
            raise serializers.ValidationError('上传失败')
        # 6、提取图片链接地址
        path = res.get('Remote file_id')

        # 7、保存图片表
        instance.logo = path

        # 更新图片
        instance.save()
        # 生成静态化页面
        # get_detail_html(sku.id)

        # 异步处理调用
        # get_detail_html.delay(name)
        return instance
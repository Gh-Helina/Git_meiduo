from rest_framework import serializers

from apps.goods.models import SKUImage, SKU


class ImageSeriazlier(serializers.ModelSerializer):
    sku=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=SKUImage
        fields=('sku','id','image')


 ##########商品序列化器###
class SKUSeriazlier(serializers.ModelSerializer):
    class Meta:
        model=SKU
        fields='__all__'
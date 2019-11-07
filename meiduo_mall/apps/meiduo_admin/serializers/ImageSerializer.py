from rest_framework import serializers

from apps.goods.models import SKUImage


class ImageSeriazlier(serializers.ModelSerializer):
    sku=serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model=SKUImage
        fields=('sku','id','image')
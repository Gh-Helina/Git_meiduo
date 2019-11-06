from rest_framework import serializers

from apps.goods.models import GoodsVisitCount

###########统计商品分类访问量序列化器#################
class GoodsSerializer(serializers.ModelSerializer):
    # 指定返回分类名称
    # 根据StringRelatedField重写返回名称
    category = serializers.StringRelatedField(read_only=True)

    class Meta:
        # 因为模型里外键返回的是ID形式,根据GoodsVisitCount模型生成序列化字段
        model = GoodsVisitCount
        # 指定返回字段
        fields = ('count', 'category')

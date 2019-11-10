from rest_framework import serializers

from apps.goods.models import SPU, Brand, GoodsCategory


########SPU商品序列化器###############
class SPUGoodSerializer(serializers.ModelSerializer):
    # 关联的品牌id
    brand_id = serializers.IntegerField()
    # 关联的品牌，名称
    brand = serializers.StringRelatedField(read_only=True)
    # 必传，不需要验证，只需要返回
    category1 = serializers.StringRelatedField(read_only=True)
    category2 = serializers.StringRelatedField(read_only=True)
    category3 = serializers.StringRelatedField(read_only=True)
    # 一级分类id
    category1_id = serializers.IntegerField()
    # 二级分类id
    category2_id = serializers.IntegerField()
    # 三级级分类id
    category3_id = serializers.IntegerField()

    class Meta:
        model = SPU
        fields = '__all__'
        #重写
        # exclude=(category1,category2,category3)


########品牌序列化器###############
class SPUBrandsSerizliser(serializers.ModelSerializer):
    """
        SPU表品牌序列化器
    """

    class Meta:
        model = Brand
        fields = "__all__"


class CategorysSerizliser(serializers.ModelSerializer):
    """
        SPU表分类信息获取序列化器
    """

    class Meta:
        model = GoodsCategory
        fields = "__all__"

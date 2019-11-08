from rest_framework import serializers

from apps.goods.models import SKUSpecification, SKU

# 定义一个序列化器的方式返回字段
class SKUSpecificationSerialzier(serializers.ModelSerializer):
    """
     SKU规格表序列化器(tb_sku_specification)
   """
    # 规格id
    spec_id = serializers.IntegerField(read_only=True)
    # 选项id
    option_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = SKUSpecification  # SKUSpecification中sku外键关联了SKU表
        fields = ("spec_id", 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    """
    #         获取sku表信息的序列化器
    #     """


    # sku作为子表嵌套返回父表spu和category
    # 指定所关联的spu表信息
    spu_id = serializers.IntegerField()
    # 关联嵌套返回
    spu = serializers.StringRelatedField(read_only=True)
    # 关联嵌套返回
    category = serializers.StringRelatedField(read_only=True)
    # 指定分类信息
    category_id = serializers.IntegerField()
    # SKUSpecification里sku有related_name=specs,子表字段内容
    # sku作为父表嵌套返回子表specs
    specs = SKUSpecificationSerialzier(read_only=True, many=True)

    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'

from rest_framework import serializers

from apps.goods.models import SKUSpecification, SKU, GoodsCategory, SpecificationOption, SPUSpecification


class SKUSpecificationSerializer(serializers.ModelSerializer):
    """
           SKU具体规格序列化器
    """
    spec_id = serializers.IntegerField()
    option_id = serializers.IntegerField()

    class Meta:
        model = SKUSpecification
        fields = ('spec_id', 'option_id')


class SKUSerializer(serializers.ModelSerializer):
    '''
    获取sku表信息的序列化器
    '''

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
    # 关联sku具体规格表
    specs = SKUSpecificationSerializer(many=True)

    class Meta:
        model = SKU  # SKU表中category外键关联了GoodsCategory分类表。spu外键关联了SPU商品表
        fields = '__all__'

    # 重写父类保存方法完成sku表和sku具体规格表两张表
    def create(self, validated_data):
        # 1、获取specs数据
        specs = validated_data.get('specs')
        # 2、将specs数据从validated_data删除
        del validated_data['specs']
        # 保存sku表数据
        # 调用父类表中的create，得到sku
        sku = super().create(validated_data)
        # 保存sku具体规格表数据。因为返回的是字典，所以下面是字典形式
        for spec in specs:
            SKUSpecification.objects.create(sku=sku, spec_id=spec['spec_id'], option_id=spec['option_id'])

        return sku

#########三级分类序列化器#################
class GoodsCategoryserializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'


class SPUOptineSerializer(serializers.ModelSerializer):
    '''
     规格选项序列化器
    '''

    class Meta:
        model = SpecificationOption
        fields = ('id', 'value')


# 序列化器的第三种定义一个序列化器的方式返回specs字段
class SPUSpecificationSerialzier(serializers.ModelSerializer):
    """
     SKU规格表序列化器(tb_sku_specification)
    """
    # 关联序列化返回 规格选项信息
    options = SPUOptineSerializer(many=True)  # 使用规格选项序列化器

    spu_id = serializers.IntegerField()
    # 关联嵌套返回
    spu = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = SPUSpecification  # SKUSpecification中sku外键关联了SKU表
        fields = '__all__'

from rest_framework import serializers

from apps.goods.models import SPUSpecification, SPU


class SPUSpecificationSerializer(serializers.ModelSerializer):
    '''
       SPU商品规格序列化器
       '''
    # 关联嵌套返回spu表的商品名
    spu = serializers.StringRelatedField(read_only=True)
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification
        fields = '__all__'

 #操作SPU商品的
class SPUSerializer(serializers.ModelSerializer):
    '''
    SPU商品序列化器
    '''
    class Meta:
        model = SPU
        fields=('id','name')
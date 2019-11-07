from rest_framework import serializers

from apps.goods.models import SpecificationOption


class SpecificationOptionSerializer(serializers.ModelSerializer):
    '''
       SPU商品规格序列化器
       '''
    # 关联嵌套返回spu表的商品名
    spec = serializers.StringRelatedField(read_only=True)
    spec_id = serializers.IntegerField()

    class Meta:
        model = SpecificationOption
        fields = '__all__'

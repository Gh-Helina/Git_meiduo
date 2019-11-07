import re
from rest_framework import serializers

from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
    # 用户表序列化器

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'password')

        # username字段增加长度限制，password字段只参与保存，不在返回给前端，增加write_only选项参数
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8
            },
            'username': {
                'max_length': 20,
                'min_length': 5
            },
        }

        # 手机号验证方法

    def validate_mobile(self, attrs):
        if not re.match(r'1[3-9]\d{9}', attrs):
            raise serializers.ValidationError('手机号格式不正确')
        return attrs
            # 重写create方法
            # 方法在ModelSerializer里没有对密码进行加密
            # # 保存用户数据并对密码加密

    def create(self, validated_data):
        # 调用父类方法获取保存后的用户对象
        user = super().create(validated_data)
        # 用户对象中的set_password方法进行密码加密
        user.set_password(validated_data['password'])
        user.save()
        return user

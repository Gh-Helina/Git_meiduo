import re
from rest_framework import serializers

from apps.users.models import User


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email', 'password')

        # username字段增加长度限制，password字段只参与保存，不在返回给前端，增加write_only选项参数
        extra_kwargs = {
            'password': {
                'write_only': True,
                'max_length': 20,
                'min_length': 8,
                # 可修改可不修改
                'required': False
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
        # 重写父类方法，增加管理员权限属性

    def create(self, validated_data):
        # 添加管理员字段
        validated_data['is_staff'] = True
        # 调用父类方法创建管理员用户
        admin = super().create(validated_data)
        # 用户密码加密
        password = validated_data['password']
        admin.set_password(password)
        # admin.is_staff = True
        admin.save()
        return admin
    def update(self, instance, validated_data):
        # 调用父类方法更新管理员用户
        instance = super().update(instance,validated_data)
        password=validated_data.get('password')
        if password:
            instance.set_password(validated_data['password'])
            instance.save()
        return instance
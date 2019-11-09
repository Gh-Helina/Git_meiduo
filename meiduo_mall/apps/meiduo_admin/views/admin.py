from django.contrib.auth.models import Group
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.AdminSelializer import AdminSerializer
from apps.meiduo_admin.serializers.GroupsSerializer import GroupSerialzier
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User


class AdminView(ModelViewSet):
    serializer_class = AdminSerializer
    # 获取管理员用户
    queryset = User.objects.filter(is_staff=True)
    pagination_class = PageNum

    # 获取分组数据
    def simple(self, reqeust):
        pers = Group.objects.all()
        ser = GroupSerialzier(pers, many=True)
        return Response(ser.data)

    # 重写父类方法，增加管理员权限属性
    def create(self, validated_data):
        # 添加管理员字段
        # validated_data['is_staff'] = True
        # 调用父类方法创建管理员用户
        admin = super().create(validated_data)
        # 用户密码加密
        password = validated_data['password']
        admin.set_password(password)
        admin.save()
        return admin
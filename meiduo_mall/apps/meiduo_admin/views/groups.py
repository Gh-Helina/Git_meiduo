from django.contrib.auth.models import Group, Permission
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.GroupsSerializer import GroupSerialzier
from apps.meiduo_admin.serializers.PermissionSerializer import PermissionSerialzier
from apps.meiduo_admin.utils import PageNum


class GroupView(ModelViewSet):
    serializer_class = GroupSerialzier
    queryset = Group.objects.all()
    pagination_class = PageNum

    # 获取权限表数据
    def simple(self, reqeust):
        pers = Permission.objects.all()
        ser = PermissionSerialzier(pers, many=True)  # 使用以前定义的全选序列化器
        return Response(ser.data)
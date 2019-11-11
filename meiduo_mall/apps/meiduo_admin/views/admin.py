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


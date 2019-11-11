from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.meiduo_admin.serializers.PermissionSerializer import PermissionSerialzier, ContentTypeSerialzier
from apps.meiduo_admin.utils import PageNum


class PermissionView(ModelViewSet):
    serializer_class = PermissionSerialzier
    queryset = Permission.objects.all()
    pagination_class = PageNum

    # 获取权限类型数据
    def content_types(self, request):
        # 查询全选分类
        content = ContentType.objects.all()
        # 返回结果
        ser = ContentTypeSerialzier(content, many=True)
        return Response(ser.data)
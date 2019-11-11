from django.contrib.auth.models import Permission
from rest_framework import serializers


class PermissionSerialzier(serializers.ModelSerializer):
    '''
   用户权限表序列化器
    '''

    class Meta:
        model=Permission
        fields="__all__"


from django.contrib.auth.models import Permission, ContentType

class ContentTypeSerialzier(serializers.ModelSerializer):
    '''
    权限类型序列化器
    '''

    class Meta:
        model=ContentType
        fields=('id','name')
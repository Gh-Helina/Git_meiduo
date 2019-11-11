from fdfs_client.client import Fdfs_client
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from apps.goods.models import Brand
from apps.meiduo_admin.serializers.BrandsSerializer import BrandsSerializer
from apps.meiduo_admin.utils import PageNum

class BrandsView(ModelViewSet):
    serializer_class = BrandsSerializer
    queryset = Brand.objects.all()
    pagination_class = PageNum


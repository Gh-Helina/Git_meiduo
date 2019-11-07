
from rest_framework.generics import ListCreateAPIView
from apps.meiduo_admin.serializers.Userserializer import UserSerializer
from apps.meiduo_admin.utils import PageNum
from apps.users.models import User


class UserView(ListCreateAPIView):
    # 指定序列化器
    serializer_class = UserSerializer
    # 指定字符集
    queryset = User.objects.filter(is_staff=False)
    # 指定分页器

    pagination_class = PageNum


# 重写get_queryset
    def get_queryset(self):
        keyword=self.request.query_params.get('keyword')
        if keyword is '' or keyword is None:
            return User.objects.filter(is_staff=False)
        else:
            return User.objects.filter(is_staff=False,username__contains=keyword)
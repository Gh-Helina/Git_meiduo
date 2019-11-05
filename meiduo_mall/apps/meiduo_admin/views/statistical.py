from datetime import date

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.users.models import User

###########普通用户总数量##################
class UserTotalCountView(APIView):
    def get(self, request):
        # 1.查询用户表获取用户总数
        count = User.objects.filter(is_staff=False,).count()
        # 2.返回用户数量
        return Response({
            'count': count

        })

###########日注册用户总数量##################
class UserDayCountView(APIView):
    def get(self, request):

        # 1.获取当前日期
        now_date=date.today()
        # 2.获取当日注册用户数量 date_joined 记录创建账户时间。数据库表有
        count=User.objects.filter(is_staff=False,date_joined__gte=now_date).count()
        # 3.返回用户数量
        return Response({
            'count': count,
            'date':now_date
        })
###########日登录用户总数量##################
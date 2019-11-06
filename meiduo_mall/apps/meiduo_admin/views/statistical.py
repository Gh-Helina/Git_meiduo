from datetime import date, timedelta

from rest_framework.response import Response
from rest_framework.views import APIView

from apps.goods.models import GoodsVisitCount
from apps.meiduo_admin.serializers.GoodsDaySerializer import GoodsSerializer
from apps.users.models import User


###########普通用户总数量##################
class UserTotalCountView(APIView):
    def get(self, request):
        # 1.查询用户表获取用户总数
        count = User.objects.filter(is_staff=False, ).count()
        # 2.返回用户数量
        return Response({
            'count': count

        })


###########日注册用户总数量##################
class UserDayCountView(APIView):
    def get(self, request):
        # 1.获取当前日期
        now_date = date.today()
        # 2.获取当日注册用户数量 date_joined 记录创建账户时间。数据库表有
        count = User.objects.filter(is_staff=False, date_joined__gte=now_date).count()
        # 3.返回用户数量
        return Response({
            'count': count,
            'date': now_date
        })


###########日登录用户总数量##################
class UserActiveCountView(APIView):
    def get(self, request):
        # 1.获取当前日期
        now_date = date.today()
        # 获取当日登录用户数量  last_login记录最后登录时间,数据库表有
        count = User.objects.filter(is_staff=False, last_login__gte=now_date).count()
        # 3.返回用户数量
        return Response({
            'count': count,
            'date': now_date
        })


###########日下单用户总数量##################
class UserOrderCountView(APIView):
    # 指定管理员权限
    # permission_classes = [IsAdminUser]

    def get(self, request):
        # 获取当前日期
        now_date = date.today()
        # 获取当日下单用户数量  orders__create_time 订单创建时间
        # 关联过滤查询 orderinfo__加表字段
        # orders是apps里orders目录
        users = set(User.objects.filter(is_staff=False, orders__create_time__gte=now_date))
        count = len(users)
        return Response({
            "count": count,
            "date": now_date
        })


###########统计月增用户总数量#################
class UserMonthCountView(APIView):
    def get(self, request):
        # 1.获取当前日期
        new_date = date.today()

        # 2.# 获取一个月前日期
        old_date = new_date - timedelta(30)

        # 3.创建空列表保存每天的用户量
        date_list = []

        for i in range(30):
            # 4.循环遍历获取当天日期
            index_date = old_date + timedelta(i)

            # 5.指定下一天日期
            next_date = old_date + timedelta(i + 1)

            #             # 查询条件是大于一个月的当前日期index_date，小于明天日期的用户next_date，得到当天用户量
            count = User.objects.filter(is_staff=False, date_joined__gte=index_date, date_joined__lt=next_date).count()
            date_list.append({
                # 当天的数量
                "count": count,
                # 当天日期
                "date": index_date
            })
        # 6.返回结果
        return Response(date_list)

###########统计商品分类访问量#################
# class GoodsDayView(APIView):
#     def get(self, request):
#         # 获取当天日期
#         now_date = date.today()
#         # 获取当天访问的商品分类数量信息
#         # GoodsVisitCount   (good/models/)
#         # goodvist获取分类数量统计的对象，返回表每个字段的内容
#         goodvist = GoodsVisitCount.objects.filter(date__gte=now_date)
#         data_list = []
#         for goods in goodvist:
#             data_list.append({
#                 'count': goods.count,
#                 'cetegory': goods.category.name  # 获取分类外键(category)获取分类名称
#             })
#         return Response(data_list)
###########统计商品分类访问量#################
class GoodsDayView(APIView):
    def get(self, request):
        # 获取当天日期
        now_date = date.today()
        # 获取当天访问的商品分类数量信息
        data = GoodsVisitCount.objects.filter(date=now_date)
        # 序列化返回分类数量
        ser = GoodsSerializer(data, many=True)

        return Response(ser.data)

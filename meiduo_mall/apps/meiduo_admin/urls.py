from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token

from apps.meiduo_admin.views import statistical
from . import views

urlpatterns = [
    url(r'^authorizations/$', obtain_jwt_token),
    # 普通用户统计路由
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    # 日注册用户统计路由：
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 当天登录用户路由：
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    # 当天下订单的用户路由：
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),

]

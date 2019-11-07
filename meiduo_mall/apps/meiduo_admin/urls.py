from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.meiduo_admin.views import spes
from apps.meiduo_admin.views import statistical, users, options

from . import views

urlpatterns = [
    # --------数据统计----------
    url(r'^authorizations/$', obtain_jwt_token),
    # 普通用户统计路由
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    # 日注册用户统计路由
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # 当天登录用户路由
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    # 当天下订单的用户路由
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    # 注册用户统计路由
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # 日商品访问量
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),

    # --------用户管理----------
    url(r'^users/$', users.UserView.as_view()),
    # SPU商品路由：
    # 视图集所以用get
    url(r'^goods/simple/$', spes.SpecsView.as_view({'get': 'simple'})),
    # 商品SpecificationOption
    url(r'^goods/specs/simple/$', options.OptionView.as_view({'get': 'simple'})),

]

# ----------商品规格表----------------
router = DefaultRouter()
router.register('goods/specs', spes.SpecsView, base_name='specs')
urlpatterns += router.urls

# ----------商品规格选项表----------------
router = DefaultRouter()
router.register('specs/options', options.OptionView, base_name='options')
urlpatterns += router.urls

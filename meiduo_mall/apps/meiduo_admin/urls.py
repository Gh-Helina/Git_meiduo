from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token

from apps.meiduo_admin.views import brands
from apps.meiduo_admin.views import images
from apps.meiduo_admin.views import orders
from apps.meiduo_admin.views import permission
from apps.meiduo_admin.views import sku
from apps.meiduo_admin.views import spes
from apps.meiduo_admin.views import spu
from apps.meiduo_admin.views import groups
from apps.meiduo_admin.views import admin

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

    # ---------商品管理---------
    # 商品规格SPU商品路由：视图集所以用get
    url(r'^goods/simple/$', spes.SpecsView.as_view({'get': 'simple'})),
    # 商品规格选项SPU商品
    url(r'^goods/specs/simple/$', options.OptionView.as_view({'get': 'simple'})),

    # 图片SPU商品
    url(r'^skus/simple/$', images.ImageView.as_view({'get': 'simple'})),
    # sku表获取三级分类路由
    url(r'^skus/categories/$', sku.SKUGoodsView.as_view({'get': 'catrgoties'})),
    # 获取spu规格信息路由
    url(r'^goods/(?P<pk>\d+)/specs/$', sku.SKUGoodsView.as_view({'get': 'specs'})),

    # ---------SPU中品牌管理---------
    # 获取品牌信息
    url(r'^goods/brands/simple/$', spu.SPUGoodsView.as_view({'get': 'brands'})),
    # # 获取一级分类
    url(r'^goods/channel/categories/$', spu.SPUGoodsView.as_view({'get': 'channel'})),
    # # 获取二三级分类
    url(r'^goods/channel/categories/(?P<pk>\d+)/$', spu.SPUGoodsView.as_view({'get': 'channels'})),
    # 新增详情介绍图片路径
    url(r'^goods/images/$', spu.SPUGoodsView.as_view({'post': 'image'})),
    # 品牌图片
    # url(r'^goods/brands/$', brands.BrandsView.as_view({'post': 'image'})),



    # ---------订单管理---------
    # 修改订单状态
    # url(r'^orders/(?P<order_id>\d+)/status/$', orders.OrdersView.as_view({'get': 'status'})),

    # ---------权限管理---------
    # 权限管理获得权限
    url(r'^permission/content_types/$', permission.PermissionView.as_view({'get': 'content_types'})),

    # ---------用户组管理---------
    # 用户组获取权限表数据
    url(r'^permission/simple/$', groups.GroupView.as_view({'get': 'simple'})),

    # ---------管理员分组管理---------
    # 获取分组信息
    url(r'^permission/groups/simple/$', admin.AdminView.as_view({'get': 'simple'})),

]

# ----------商品规格表----------------
router = DefaultRouter()
router.register('goods/specs', spes.SpecsView, base_name='specs')
urlpatterns += router.urls

# ----------商品规格选项表----------------

router.register('specs/options', options.OptionView, base_name='options')
urlpatterns += router.urls

# ----------图片表----------------

router.register('skus/images', images.ImageView, base_name='images')
urlpatterns += router.urls

# ----------SKU表----------------

router.register('skus', sku.SKUGoodsView, base_name='skus')
urlpatterns += router.urls

# ----------品牌表----------------
router.register('goods/brands', brands.BrandsView, base_name='brands')
urlpatterns += router.urls

# ----------频道管理表----------------
router.register('goods/brands', brands.BrandsView, base_name='brands')
urlpatterns += router.urls

# ----------SPU表----------------
router.register('goods', spu.SPUGoodsView, base_name='spus')
urlpatterns += router.urls

# ----------Orders表----------------

router.register('orders', orders.OrdersView, base_name='orders')
urlpatterns += router.urls

# ----------权限管理表----------------

router.register('permission/perms', permission.PermissionView, base_name='permissions')
urlpatterns += router.urls

# ----------用户组管理表----------------

router.register('permission/groups', groups.GroupView, base_name='groups')
urlpatterns += router.urls

# ----------管理员管理表----------------

router.register('permission/admins', admin.AdminView, base_name='admin')
urlpatterns += router.urls

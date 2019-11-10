from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.meiduo_admin.serializers.OrdersSerializer import OrderSeriazlier
from apps.meiduo_admin.utils import PageNum

from apps.orders.models import OrderInfo


class OrdersView(ModelViewSet):
    serializer_class = OrderSeriazlier
    queryset = OrderInfo.objects.all()
    pagination_class = PageNum

    # 重写get_queryset
    ######搜索##########
    def get_queryset(self):
        keyword = self.request.query_params.get('keyword')
        if keyword is '' or keyword is None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)

    ######在视图中定义status方法修改订单状态######

    # detail生成一个正则匹配，匹配pk
    # 只有前缀 + 方法名才可以用自动生成路由
    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        try:
            # 获取订单对象
            order = OrderInfo.objects.get(order_id=pk)
        except:
            return Response({'error': '订单信息错误'}, status=400)
        # 获取要修改的状态值
        status = request.data.get('status')
        # 修改订单状态
        order.status = status
        order.save()
        # 返回结果
        # ser = self.get_serializer(order)
        return Response({
            'order_id': order.order_id,
            'status': status
        })

from ..models.order import Order
from rest_framework.viewsets import ModelViewSet
from ..serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer
    queryset = Order.objects.all()
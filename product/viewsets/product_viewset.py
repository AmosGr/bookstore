from product.models import Product
from product.serializers.product_serializers import ProductSerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet): 

    serializer_class = ProductSerializer

    def get_queryset(self):
        return Product.objects.all()


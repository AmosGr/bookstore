from rest_framework import serializers
from product.models.product import Product
from product.models.category import Category
from product.serializers.category_serializers import CategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True, many=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(),write_only=True,many=True)

    class Meta: 
        model = Product
        fields = [
            'title',
            'description'
            'price',
            'active',
            'category',
        ]
    
    def create(self, validated_data):
        category_data = validated_data.pop('category_id')

        product = Product.objects.create(**validated_data)
        for category in category_data:
            product.category.add(category)
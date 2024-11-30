from rest_framework import serializers

from product.models import Product , product_category


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = product_category
        fields = '__all__'


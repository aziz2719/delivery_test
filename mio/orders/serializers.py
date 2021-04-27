from rest_framework import serializers
from .models import Order, OrderProduct
from products.models import Product


class OrdersProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price')


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'product', 'order', 'good_quantity')


class OrderSerializer(serializers.ModelSerializer):
    prodect_order_product = OrderProductSerializer(many=True)

    class Meta:
        model = Order
        fields = ('id', 'date', 'address', 'total_price', 'status', 'prodect_order_product')

    def create(self, validated_data):
        print(validated_data)
        products = validated_data.pop('prodect_order_product')
        print(validated_data)
        order = Order.objects.create(**validated_data)
        for product in products:
            prodect_order = OrderProduct.objects.create(**product)
            prodect_order.order = order
            prodect_order.save()
        order.set_total_price()
        return order

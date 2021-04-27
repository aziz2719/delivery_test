from rest_framework import serializers
from .models import Product
from .models import ProductImage
from .models import ProductMark


class ProductImagesSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ProductImage
        fields = ('__all__')


class ProductMarkSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = ProductMark
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True, format='%d.%m.%Y %H:%M')
    product_marks = ProductMarkSerializer(read_only=True, many=True)
    user_marks = ProductMarkSerializer(many=True)
    product_image = ProductImagesSerializer(read_only=True, many=True)
    class Meta:
        model = Product
        fields = (
            'id', 'name', 'text', 'price', 'category',
            'rating', 'created_at', 'product_marks', 'user_marks', 'product_image',
        )


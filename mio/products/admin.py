from django.contrib import admin
from .models import Product, ProductMark, ProductImage

admin.site.register(Product)
admin.site.register(ProductMark)
admin.site.register(ProductImage)
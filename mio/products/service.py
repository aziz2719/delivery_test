from django_filters import rest_framework as filters
from .models import Product

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class ProductFilter(filters.FilterSet):
    price = filters.RangeFilter(field_name='price', lookup_expr='in')#(field_name='price', lookup_expr='in')
    class Meta:
        model = Product
        fields = ['price']
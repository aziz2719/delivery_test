from django_filters import rest_framework as filters
from .models import Category

class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CategoryFilter(filters.FilterSet):
    category = CharFilterInFilter(field_name='category', lookup_expr='in')
    class Meta:
        model = Category
        fields = ['category']
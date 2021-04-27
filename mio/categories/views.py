from django.shortcuts import render

from .models import Category
from .serializers import CategorySerializer
from .permissions import IsOwnerUserOrReadOnly

from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView, Response

from django_filters.rest_framework import DjangoFilterBackend
from .service import CategoryFilter


class CategoriesView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsOwnerUserOrReadOnly, )
    filter_backends = (DjangoFilterBackend, )
    filter_class = CategoryFilter
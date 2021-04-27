from django.urls import path
from .views import OrderView
from rest_framework import routers


router = routers.DefaultRouter()
router.register('', OrderView)

urlpatterns = []
urlpatterns += router.urls

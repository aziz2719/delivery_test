from django.urls import path
from .views import ProductsView
from .views import ProductMarkView

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', ProductsView)



urlpatterns = [
    path('marks', ProductMarkView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += router.urls
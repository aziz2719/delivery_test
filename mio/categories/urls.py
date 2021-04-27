from django.urls import path
from .views import CategoriesView
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', CategoriesView)



urlpatterns = [
    path('', CategoriesView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += router.urls
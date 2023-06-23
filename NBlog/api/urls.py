from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'post', views.PostViewSet)

urlpatterns = [
    path('def-auth/', include('rest_framework.urls')),
    path('', include(router.urls)),

]

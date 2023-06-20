from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register(r'post', views.PostViewSet)



urlpatterns = [
    # path('postlist', views.PostAPIList.as_view()),
    # path('postlist/<str:pk>', views.PostAPIDetailView.as_view()),

    # path('postlist', views.PostViewSet.as_view({'get': 'list'})),
    # path('postlist/<str:pk>', views.PostViewSet.as_view({'put': 'update'})),
    path('def-auth/', include('rest_framework.urls')), # Session-based authentication
    path('', include(router.urls)),

]

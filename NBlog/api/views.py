from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializer
from ..models import Post


class PostAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = PostAPIListPagination

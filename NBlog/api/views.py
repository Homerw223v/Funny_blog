from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework import generics, viewsets

from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly
from .serializers import PostSerializer
from ..models import Bloger, Post, Comment
from rest_framework.response import Response


# generics.CreateAPIView                    Создание данных по POST-запросу
# ----------------------------------------------------------------------------------------------------------------------
# generics.ListAPIView                      Чтение списка данных по GET-запросу
# ----------------------------------------------------------------------------------------------------------------------
# generics.RetrieveAPIView                  Чтение конкретных данных(записи) по GET-запросу
# ----------------------------------------------------------------------------------------------------------------------
# generics.DestroyAPIView                   Удаление данных(записи) по DELETE-запросу
# ----------------------------------------------------------------------------------------------------------------------
# generics.UpdateAPIView                    Изменение записи по PUT или PATCH-запросу
# ----------------------------------------------------------------------------------------------------------------------
# generics.ListCreateAPIView                Для чтения(по GET-запросу) и создание списка данных(по POST-запросу)
# ----------------------------------------------------------------------------------------------------------------------
# generics.RetrieveUpdateAPIView            Чтение и изменение отдельной записи(GET и POST-запрос)
# ----------------------------------------------------------------------------------------------------------------------
# generics.RetrieveDestroyAPIView           Чтение(GET-запрос) и удаление(DELETE-запрос) отдельной записи
# ----------------------------------------------------------------------------------------------------------------------
# generics.RetrieveUpdateDestroyAPIView     Чтение, изменение и добавление отдельной записи(GET, PUT, PATCH, DELETE-запросы)

# class PostAPIList(generics.ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIUpdate(generics.UpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#
# class PostAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

class PostAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 1000
    # invalid_page_message = 'Gomu Gomu Noooooo Pistolet'


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    pagination_class = PostAPIListPagination

# class PostAPI(APIView):
#     def get(self, request, pk=None):
#         if pk:
#             post = Post.objects.get(title=pk)
#             return Response({'post': PostSerializer(post).data})
#         else:
#             posts = Post.objects.all()
#         return Response({'posts': PostSerializer(posts, many=True).data})
#
#     def post(self, request):
#         serializer = PostSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'posts': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method PUT now allowed'})
#         try:
#             instance = Post.objects.get(title=pk)
#             serializer = PostSerializer(data=request.data, instance=instance)
#             serializer.is_valid(raise_exception=True)
#             serializer.save()
#             return Response({'post': serializer.data})
#         except:
#             return Response({'error': 'Object does not exists'})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'Method DELETE now allowed'})
#         try:
#             instance = Post.objects.get(title=pk)
#             instance.delete()
#         except:
#             return Response({'error': 'Object does not exists'})

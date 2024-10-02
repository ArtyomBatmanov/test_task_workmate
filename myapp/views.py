from rest_framework import generics, permissions, viewsets
from .models import Kitten, Breed, Rating
from .serializers import KittenSerializer, BreedSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response


class BreedListView(generics.ListCreateAPIView):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class KittenListView(generics.ListCreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class KittenDetailView(viewsets.ModelViewSet):
#     queryset = Kitten.objects.all()
#     serializer_class = KittenSerializer
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def get_queryset(self):
#         # Возвращаем всех котят, но вы можете добавить здесь логику для ограничения
#         return Kitten.objects.all()  # Здесь вы можете возвращать всех котят
#
#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         # Проверка на то, является ли пользователь владельцем, если это требуется
#         if instance.owner != request.user:
#             self.check_object_permissions(request, instance)
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)


class KittenDetailView(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Kitten.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            self.check_object_permissions(request, instance)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            self.check_object_permissions(request, instance)
        serializer = self.get_serializer(instance, data=request.data, partial=False)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.owner != request.user:
            self.check_object_permissions(request, instance)
        self.perform_destroy(instance)
        return Response(status=204)


class KittenBreedListView(generics.ListAPIView):
    serializer_class = KittenSerializer

    def get_queryset(self):
        queryset = Kitten.objects.all()
        breed = self.request.query_params.get('breed')
        if breed is not None:
            queryset = queryset.filter(breed__id=breed)
        return queryset


class KittenCreateView(generics.CreateAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    permission_classes = [IsAuthenticated]




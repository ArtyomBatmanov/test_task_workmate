from rest_framework import generics, permissions
from .models import Kitten, Breed, Rating
from .serializers import KittenSerializer, BreedSerializer, RatingSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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

class KittenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Kitten.objects.filter(owner=self.request.user)

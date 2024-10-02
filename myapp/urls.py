from django.urls import path
from .views import BreedListView, KittenListView, KittenDetailView, KittenBreedListView, KittenCreateView
urlpatterns = [
    path('breeds/', BreedListView.as_view(), name='breed-list'),
    path('kittens/', KittenListView.as_view(), name='kitten-list'),
    path('kittens/<int:pk>/', KittenDetailView.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='kitten-detail'),  # Поддержка GET, PUT, DELETE    path('kittens/?breed=<breed_id>', KittenBreedListView.as_view(), name='kitten_breed_list'),
    path('kittens/', KittenCreateView.as_view(), name='kitten-create'),
    path('kittens/?breed=<breed_id>', KittenBreedListView.as_view(), name='kitten_breed_list'),
]


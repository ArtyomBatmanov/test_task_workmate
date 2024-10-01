from django.urls import path
from .views import BreedListView, KittenListView, KittenDetailView

urlpatterns = [
    path('breeds/', BreedListView.as_view(), name='breed-list'),
    path('kittens/', KittenListView.as_view(), name='kitten-list'),
    path('kittens/<int:pk>/', KittenDetailView.as_view(), name='kitten-detail'),
]

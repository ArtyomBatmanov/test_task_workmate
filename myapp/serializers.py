from rest_framework import serializers
from .models import Kitten, Breed, Rating


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ['id', 'name']


class KittenSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Kitten
        fields = ['id', 'breed', 'color', 'age_in_months', 'description', 'owner']


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['kitten', 'user', 'score']





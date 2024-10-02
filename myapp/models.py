from django.db import models
from django.contrib.auth.models import User


class Breed(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Kitten(models.Model):
    COLOR_CHOICES = [
        ('чёрный', 'Чёрный'),
        ('белый', 'Белый'),
        ('серый', 'Серый'),
    ]

    breed = models.ForeignKey(Breed, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    age_in_months = models.PositiveIntegerField()
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.breed.name} - {self.color} - {self.age_in_months} months"


class Rating(models.Model):
    kitten = models.ForeignKey(Kitten, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    class Meta:
        unique_together = ('kitten', 'user')

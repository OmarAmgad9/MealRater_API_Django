from django.shortcuts import render
from .models import Rating, Meal
from .serializers import MealSerializers, RatingSerializers

from rest_framework import viewsets

# CRUD operation from model
class ViewSets_Meal(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers

class ViewSets_Rating(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers

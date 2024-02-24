from rest_framework import serializers
from  .models import Rating, Meal


class MealSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meal
        fields = ["id", "title", "description", "no_of_rating", "avg_rating"]

class RatingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"
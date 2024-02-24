from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import status
from .models import Rating, Meal
from rest_framework.response import Response
from .serializers import MealSerializers, RatingSerializers
from django.contrib.auth.models import User
from rest_framework import viewsets

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

# CRUD operation from model
class ViewSets_Meal(viewsets.ModelViewSet):
    queryset = Meal.objects.all()
    serializer_class = MealSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]
    @action( detail=True,methods=['POST'])
    def rate_meal(self, request, pk=None):
        if 'stars' in request.data:
            """
            Create Or Update
            """
            meal = Meal.objects.get(id=pk)
            username = request.data['username']
            stars = request.data['stars']
            user = User.objects.get(username=username)
            try:
                # Check if PK Founded make Update 
                # Meal , User , Stars
                rate = Rating.objects.get(user=user.id, meal=meal.id)
                rate.starts = stars
                rate.save()
                serializer = RatingSerializers(rate, many=False)
                json = {
                    'message': "Meal Rate Update",
                    'result': serializer.data,
                }
                return Response(json, status=status.HTTP_200_OK)
            except:
                # If Pk No Found make Rating
                rating = Rating.objects.create(user=user.id,meal=meal.id, stars=stars)
                rating.save()
                serializer = RatingSerializers(rate, many=False)
                json = {
                    'message': "Meal Rate Create",
                    'result' : serializer.data
                }
            return Response(json, status=status.HTTP_200_OK)
        else:
            json = {
                "Message": "Stars Not Provided"
            }
            return Response(json, status=status.HTTP_400_BAD_REQUEST)





class ViewSets_Rating(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializers
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated]

    def update(self, request, *args, **Kwargs):
        response = {
            'Message': 'This Is Not How You Should Create Update Rating'
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)
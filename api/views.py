from django.shortcuts import render
from rest_framework import generics

from boy import models
from django.contrib.auth.models import User
from . import serializers


# Create your views here.
#Dog oparations
class ListOfDogs(generics.ListCreateAPIView):
	queryset = models.Dog.objects.all()
	serializer_class = serializers.DogSerializer    

class DetailOfDog(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()    
    serializer_class = serializers.DogSerializer

#Medication oparations
class ListOfMedication(generics.ListCreateAPIView):
	queryset = models.Medication.objects.all()
	serializer_class = serializers.MedicationSerializer    

class DetailOfMedication(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Medication.objects.all()    
    serializer_class = serializers.MedicationSerializer

#Feed oparations
class ListOfFeed(generics.ListCreateAPIView):
	queryset = models.Feed.objects.all()
	serializer_class = serializers.FeedSerializer    

class DetailOfFeed(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Feed.objects.all()    
    serializer_class = serializers.FeedSerializer

#Review oparations
class ListOfReview(generics.ListCreateAPIView):
	queryset = models.Review.objects.all()
	serializer_class = serializers.ReviewSerializer    

class DetailOfReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Dog.objects.all()    
    serializer_class = serializers.ReviewSerializer

#User oparations
class ListOfUser(generics.ListCreateAPIView):
	queryset = User.objects.all()
	serializer_class = serializers.UserSerializer    

class DetailOfUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()    
    serializer_class = serializers.UserSerializer



    

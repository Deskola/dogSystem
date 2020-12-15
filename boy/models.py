from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Dog entity.
class Dog(models.Model):
	name = models.CharField(max_length=70, blank=False, default='')
	breed = models.CharField(max_length=100, blank=False, default='')
	dob = models.DateField(blank=False, default='')
	image = models.FileField(null=True , blank=True)
	user = models.ForeignKey(User, related_name='dogs', on_delete=models.CASCADE)

#Medication details
class Medication(models.Model):
	dog = models.ForeignKey(Dog, related_name="medications", on_delete=models.CASCADE)
	medication_date = models.DateField(blank=False, default='')
	operation_type = models.CharField(max_length=70, blank=False, default='')
	details = models.CharField(max_length=100, blank=False, default='')
	cost = models.CharField(max_length=70, blank=False, default='')

#Feeds managment
class Feed(models.Model):
	user =  models.ForeignKey(User, related_name="feeds", on_delete=models.CASCADE)
	feed_name = models.CharField(max_length=100, blank=False, default='')
	feed_type = models.CharField(max_length=100, blank=False, default='')
	quantity = models.CharField(max_length=100, blank=False, default='')
	consumption_per_day = models.CharField(max_length=100, blank=False, default='')
	almost_finished = models.BooleanField(default=False)

#Vet Review
class Review(models.Model):
	user =  models.ForeignKey(User, related_name="reviews", on_delete=models.CASCADE)
	comment =  models.CharField(max_length=100, blank=False, default='')


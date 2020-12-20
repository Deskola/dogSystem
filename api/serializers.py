from rest_framework import serializers
from django.contrib.auth.models import User, Group
from boy import models


#User serialize for Json
class UserSerializer(serializers.ModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
	class Meta:
		#model to serialize
		model = User
		#a tuple of field names to be included in the serialization
		fields = '__all__'

#Dog serialize for Json
class DogSerializer(serializers.ModelSerializer):
	#url = serializers.HyperlinkedIdentityField(view_name="api:user-detail")
	class Meta:
		#model to serialize
		model = models.Dog
		#a tuple of field names to be included in the serialization
		fields = (
			'id',
			'name',
			'breed',
			'dob',
			'image',
			'user'
			
		)

#Medication serialize for Json
class MedicationSerializer(serializers.ModelSerializer):
	class Meta:
		#model to serialize
		model = models.Medication
		#a tuple of field names to be included in the serialization
		fields = (
			'id',
			'dog',
			'medication_date',
			'operation_type',
			'details',
			'cost',			
		)

#Medication serialize for Json
class MedicationForAllSerializer(serializers.ModelSerializer):
	class Meta:
		#model to serialize
		model = models.MedicationForAll
		#a tuple of field names to be included in the serialization
		fields = (
			'id',			
			'medication_date',
			'operation_type',
			'details',
			'cost',
			
		)

#Feed serialize for Json
class FeedSerializer(serializers.ModelSerializer):
	class Meta:
		#model to serialize
		model = models.Feed
		#a tuple of field names to be included in the serialization
		field = (
			'id',
			'user',
			'feed_name',
			'feed_type',
			'quantity',
			'consumption_per_day',
			'almost_finished',
			'url'

		)

#Review serialize for Json
class ReviewSerializer(serializers.ModelSerializer):
	class Meta:
		#model to serialize
		model = models.Review
		#a tuple of field names to be included in the serialization
		fields = (
			'id',
			'user',
			'comment',
			'url'
		)

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'name', 'url')

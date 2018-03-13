from rest_framework import serializers
from restaurants.models import Restaurant
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model= User
		fields= ['username','first_name','last_name']

class RestaurantListSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name= 'apilist',
		lookup_field= 'id',
		lookup_url_kwarg= 'restaurant_id',
		)
	#owner= serializers.SerializerMethodField()
	owner= UserSerializer()

	class Meta:
		model = Restaurant
		fields = ['id','name','description','owner',]

	#def get_owner(self, obj):
	#	return obj.owner.username

class RestaurantDetailSerializer(serializers.ModelSerializer):
	detail = serializers.HyperlinkedIdentityField(
		view_name= 'apidetail',
		lookup_field= 'id',
		lookup_url_kwarg= 'restaurant_id',
		)
	owner= UserSerializer()
	class Meta:
		model = Restaurant
		fields = '__all__'

class RestaurantCreateSerializer(serializers.ModelSerializer):
	class Meta:
		model= Restaurant
		fields= ['name', 'description', 'image']
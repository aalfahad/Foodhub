from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateAPIView
from restaurants.models import Restaurant
from .serializers import RestaurantListSerializer,RestaurantDetailSerializer, RestaurantCreateSerializer,UserSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .permissions import IsOwnerOrStaff
from rest_framework.filters import SearchFilter, OrderingFilter

# Create your views here.
class RestaurantListAPIView(ListAPIView):
	queryset= Restaurant.objects.all()
	serializer_class = RestaurantListSerializer
	permission_classes = [AllowAny,]
	filter_backends = [SearchFilter]
	search_fields = ['title', 'description','owner__username']

class RestaurantDetailAPIView(RetrieveAPIView):
	queryset= Restaurant.objects.all()
	serializer_class= RestaurantDetailSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'restaurant_id'
	permission_classes = [AllowAny,]

class RestaurantDeleteAPIView(DestroyAPIView):
	queryset= Restaurant.objects.all()
	serializer_class= RestaurantDetailSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'restaurant_id'
	permission_classes = [IsAuthenticated,IsOwnerOrStaff]

class RestaurantCreateAPIView(CreateAPIView):
	queryset= Restaurant.objects.all()
	serializer_class = RestaurantCreateSerializer
	permission_classes = [IsAuthenticated,IsOwnerOrStaff]

	def perform_create(self,serializer):
		#assign the owner
		serializer.save(owner=self.request.user)

class ArticleUpdateAPIView(RetrieveUpdateAPIView):
	queryset= Restaurant.objects.all()
	serializer_class= RestaurantCreateSerializer
	lookup_field= 'id'
	lookup_url_kwarg= 'restaurant_id'
	permission_classes = [IsAuthenticated,IsOwnerOrStaff]
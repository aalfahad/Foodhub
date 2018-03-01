from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __str__(self):
		return self.name

class Item(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=12, decimal_places=4)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

	def __str__(self):
		return self.name

class FavRest(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

class FavItem(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	item = models.ForeignKey(Item, on_delete=models.CASCADE)
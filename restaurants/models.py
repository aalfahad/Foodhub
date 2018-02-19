from django.db import models

class Restaurant(models.Model):
	name = models.CharField(max_length=255)
	description = models.TextField()
	image = models.ImageField(null=True, blank=True)
	opening_time = models.TimeField()
	closing_time = models.TimeField()

	def __str__(self):
		return self.name





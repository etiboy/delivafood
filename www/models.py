from __future__ import unicode_literals

from django.db import models

# Area where a kitchen is located
class Area(models.Model):
	code =  models.IntegerField(default=0)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	image = models.CharField(max_length=200)

	def __str__(self):
		return self.name
#Kitchen Details
class Kitchen(models.Model):
	area = models.ForeignKey(Area, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	photo_1 = models.CharField(max_length=200)
	photo_2 = models.CharField(max_length=200)
	photo_3 = models.CharField(max_length=200)
	photo_4 = models.CharField(max_length=200)
	photo_5 = models.CharField(max_length=200)
	last_updated = models.DateTimeField('Capture Date and Time of last update to Restaurant')

	def __str__(self):
		return self.name

class FoodCategory(models.Model):
	name = models.CharField(max_length=200)
	image = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Cuisine(models.Model):
	name = models.CharField(max_length=200)
	image = models.CharField(max_length=200)

	def __str__(self):
		return self.name

class Food(models.Model):
	VEGETARIAN_OPTIONS = (
		('Veg', 'Vegetarian'),
		('Non-Veg', 'Non Vegetarian'),
	)
	kitchen = models.ForeignKey(Kitchen, on_delete=models.SET_NULL, null=True)
	foodCategory = models.ForeignKey(FoodCategory, on_delete=models.SET_NULL, null=True)
	cuisine = models.ForeignKey(Cuisine, on_delete=models.SET_NULL, null=True)
	name = models.CharField(max_length=200)
	description = models.CharField(max_length=500)
	price = models.DecimalField(max_digits=100, decimal_places=2)
	vegetarian = models.CharField(max_length=7, choices=VEGETARIAN_OPTIONS)
	photo_1 = models.CharField(max_length=200)
	photo_2 = models.CharField(max_length=200)
	photo_3 = models.CharField(max_length=200)
	photo_4 = models.CharField(max_length=200)
	photo_5 = models.CharField(max_length=200)

	def __str__(self):
		return self.name




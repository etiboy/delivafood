from django.shortcuts import render
from .models import Kitchen,Food,Area,Cuisine,FoodCategory

# home page

def home(request,area_name,area_code='560001'):
	homePageMeals = Food.objects.filter(kitchen__area__code = area_code)
	return render(request, 'index.html', {'meals': homePageMeals})

def foodDetails(request,food_id,food_name):
	foodDetail = Food.objects.get(id  = food_id)
	return render(request, 'food.html', {'food': foodDetail})

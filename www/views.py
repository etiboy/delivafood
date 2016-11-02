from django.shortcuts import render
from .models import Kitchen,Food,Area,Cuisine,FoodCategory

# home page

def home(request):
	homePageMeals = Food.objects.filter(kitchen__area__code__contains = '560')
	return render(request, 'index.html', {'meals': homePageMeals})

def foodDetails(request,food_id,food_name):
	foodDetail = Food.objects.get(id  = food_id)
	return render(request, 'food.html', {'food': foodDetail})

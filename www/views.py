from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Kitchen,Food,Area,Cuisine,FoodCategory,TodaySpecial

# home page

def home(request):
	homePageMeals = Food.objects.filter(kitchen__area__code__contains = "560")
	todaySpecial = TodaySpecial.objects.get(pk=1)
	return render(request, 'index.html', {'meals': homePageMeals, 'special': todaySpecial.food})

def foodDetails(request,food_id,food_name):
	foodDetail = get_object_or_404(Food, pk=food_id)
	'''
	try:
		foodDetail = Food.objects.get(id  = food_id)
	except Food.DoesNotExist:
		 raise Http404("Question does not exist")
	'''
	return render(request, 'food.html', {'food': foodDetail})

def findRestaurants(request):
	return render(request, 'restaurants.html')

def homeArea(request,area_name):
	homePageMeals = Food.objects.filter(kitchen__area__name = area_name)
	todaySpecial = TodaySpecial.objects.filter(food__kitchen__area__name = area_name)
	return render(request, 'index.html', {'meals':homePageMeals, 'special': todaySpecial[0].foode})

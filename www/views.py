from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .models import Kitchen,Food,Area,Cuisine,FoodCategory

# home page

def home(request):
	homePageMeals = Food.objects.filter(kitchen__area__code__contains = "560")
	return render(request, 'index.html', {'meals': homePageMeals})

def foodDetails(request,food_id,food_name):
	foodDetail = get_object_or_404(Food, pk=food_id)
	'''
	try:
		foodDetail = Food.objects.get(id  = food_id)
	except Food.DoesNotExist:
		 raise Http404("Question does not exist")
	'''
	return render(request, 'food.html', {'food': foodDetail})

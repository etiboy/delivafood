from django.contrib import admin
from .models import Kitchen,Area,Food,FoodCategory,Cuisine,TodaySpecial
# Register your models here.
myModels = [Kitchen,Area,Food,FoodCategory,Cuisine,TodaySpecial]
admin.site.register(myModels)
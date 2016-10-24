from django.contrib import admin
from .models import Kitchen,Area,Food,FoodCategory,Cuisine
# Register your models here.
myModels = [Kitchen,Area,Food,FoodCategory,Cuisine]
admin.site.register(myModels)
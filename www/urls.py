from django.conf.urls import url
from . import views
app_name = 'www'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^area/(?P<area_name>.*)/$', views.homeArea, name='home_area'),
	url(r'^food/(?P<food_id>.*)/(?P<food_name>.*)/$', views.foodDetails, name='food_details'),
	url(r'^find-restaurants/$', views.findRestaurants, name='find-restaurants')
]
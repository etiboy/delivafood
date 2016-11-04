from django.conf.urls import url
from . import views
app_name = 'www'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^area/(?P<area_code>.*)/(?P<area_name>[-\w\d]+)/$', views.home, name='home'),
	url(r'^food/(?P<food_id>.*)/(?P<food_name>.*)/$', views.foodDetails, name='food_details')
]
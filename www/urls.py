from django.conf.urls import url
from . import views
app_name = 'www'
urlpatterns = [
	url(r'^$', views.home, name='home'),
	#url(r'^food/(?P<food_name>.*)/(?P<food_id>.*)/$', views.foodDetails, name='food_details')
	url(r'^food/(?P<food_id>.*)/(?P<food_name>.*)/$', views.foodDetails, name='food_details')
]
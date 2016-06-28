from django.conf.urls import include, url
from . views import mybotview
urlpatterns = [
	url(r'^c7af68f7798531824d2dcfca43e9ff37bf8d781f41abb27c77/?$', mybotview.as_view())
]
from django.conf.urls import url
from django.urls import path

from .views import *

urlpatterns = [
	path('get-authentication/', GetAuthentication.as_view(), name='get-authentication'),
]
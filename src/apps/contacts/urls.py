from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^contact-manager/$', views.ContactDetailsManager.as_view(), name='contact-manager'),
	# url(r'^search/$', views.SearchContact.as_view(), name='search_contact'),
]
import json
import requests

from django.conf import settings
from rest_framework import status

def get_authentication_token(params):
	"""
	Fetching Authentication token for user 
	"""
	auth = (settings.CONTACT_BOOK_OAUTH2_CLIENT_ID, settings.CONTACT_BOOK_OAUTH2_SECRECT_ID)
	response = requests.post(settings.BASE_URL + 'o/token/',
					data=params, auth=auth, verify=False)
	
	if response.status_code == status.HTTP_200_OK:
		return {'status':True, 'data': response.json()}
	
	return {'status':False, 'error': response.json().get('error_description')}
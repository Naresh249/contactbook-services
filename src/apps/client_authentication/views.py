from rest_framework import status
from rest_framework.views import APIView

from api import utils as api_utils
from client_authentication import serializers as client_authentication_sz
from client_authentication import utils as client_authentication_utils

class GetAuthentication(APIView):
	"""
	Fetching Authentication for user
	"""
	def post(self, request):
		"""
		Fetching Authentication Token for client
		 : params - username and password
		 return AuthenticationToken
		"""
		request_validator = client_authentication_sz.GetAuthenticationSerializer(
				data=request.data)
		if not request_validator.is_valid():
			return api_utils.response(
				error=request_validator.errors,
				code=status.HTTP_400_BAD_REQUEST)
		response = client_authentication_utils.get_authentication_token(request_validator.validated_data)
		if not response.get('status'):
			return api_utils.response(
					error=response.get('error'),
					code=status.HTTP_400_BAD_REQUEST)
		return api_utils.response(data=response)

from rest_framework import status
from rest_framework.response import Response

def response(data={}, code=status.HTTP_200_OK, error=""):
	"""
	Returning API Response & Errors
	"""
	res = {'error': error, 'response': data}
	return Response(data=res, status=code)
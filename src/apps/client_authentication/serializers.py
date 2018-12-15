from rest_framework import serializers

class GetAuthenticationSerializer(serializers.Serializer):
	"""
	Validating request params for get authentication
	"""
	username = serializers.CharField(max_length=255)
	password = serializers.CharField(max_length=255)

	def validate(self, data):
		"""
		Adding grant type in request
		"""
		data['grant_type'] = 'password'
		return data

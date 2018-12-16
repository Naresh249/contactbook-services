from rest_framework import permissions

class IsContactBookUser(permissions.BasePermission):
	"""
	Permissions for contact book user
	"""
	def has_permission(self, request, view):
		"""
		Checking if user is valid or not
		"""
		if request.user.is_authenticated:
			return True

	def has_object_permission(self, request, view, UserContactMapping):
		"""
		Checking object level permission
		"""
		if request.method in ['DELETE', 'PUT']:
			if UserContactMapping.user_id != request.user.id:
				return False
		return True
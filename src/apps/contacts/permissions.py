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

	def has_object_permission(self, request, view, obj):
		"""
		Checking object level permission
		"""
		return False
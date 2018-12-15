from django.db import models

class ModelBase(models.Model):
	"""
	This is a abstract model class to add is_deleted, created_at and modified at fields in any model
	"""
	is_deleted = models.BooleanField(default=False)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True

	def delete(self, *args, **kwargs):
		""" Soft delete """
		self.is_deleted = True
		self.save()

class AddressDetails(models.Model):
	"""
	Model to store - Address Details
	"""
	address = models.TextField()
	landmark = models.CharField(max_length=255, null=True, blank=True)
	city = models.CharField(max_length=255, null=True, blank=True)
	pincode = models.CharField(max_length=6, null=True, blank=True)
	state = models.CharField(max_length=255, null=True, blank=True) # for this values can be binded as well
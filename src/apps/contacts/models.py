from django.contrib.auth.models import User
from django.db import models

from api.models import ModelBase, AddressDetails

class Relationship(ModelBase):
	"""
	Model to Store Relationships
	"""
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

# A unique email id contact can be a part of multiple user contact book but contact details will be different for each
class Contact(ModelBase):
	"""
	Storing Contact Uniqueness for email
	"""
	email = models.EmailField(max_length=100,unique=True)
	is_verified = models.BooleanField(default=False)

# This is basic schema of contact details it can be improved base on proper discussion on requirements
	# where a user contact can hava multiple numbers or address as well
class ContactDetails(ModelBase, AddressDetails):
	"""
	Storing Contact Addition Details with Versioning for different User
	"""
	contact = models.ForeignKey(Contact, related_name='contact_user', on_delete=models.CASCADE)
	name = models.CharField(max_length=255) # Will store the fullname
	primary_mobile_number = models.CharField(max_length=13)
	secondary_mobile_number = models.CharField(max_length=13, null=True, blank=True)
	company_name = models.CharField(max_length=255, null=True, blank=True)
	occupation = models.CharField(max_length=255, null=True, blank=True)
	relationship = models.ForeignKey(
		Relationship, related_name='user_relationship', on_delete=models.CASCADE)

class UserContactMapping(ModelBase):
	"""
	Model to store details of user and contact
	"""
	user = models.ForeignKey(User, related_name='user_contact', on_delete=models.CASCADE)
	contact_details = models.ForeignKey(
		ContactDetails, related_name='user_contact_details', on_delete=models.CASCADE)


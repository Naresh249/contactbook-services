import copy

from django.db import transaction
from rest_framework import status
from rest_framework.views import APIView

from api import utils as api_utils
from contacts import permissions as contacts_permissions
from contacts import serializers as contacts_serializer
from contacts.models import *
from contacts import utils as contacts_utils

class ContactDetailsManager(APIView):
	"""
	Managing the contact books - CRUD 
	"""
	# Applying Permission of IsContactBookUser Class 
	permission_classes = (contacts_permissions.IsContactBookUser,)

	def get(self, request):
		"""Fetching Contacts of User"""
		import pdb;pdb.set_trace()
		data = contacts_utils.fetch_user_contacts(request.user.id)
		if not data:
			return api_utils.response(
					error='Contact is not available.',
					code=status.HTTP_400_BAD_REQUEST)

		return api_utils.response(data=data)

	def post(self, request):
		"""
		Creating Contacts for authicated user
		params: 
		"""
		params = copy.deepcopy(request.data)
		contact_details_serliazer = contacts_serializer.ContactDetailsSerializer(
			data=params, context={'user_id': request.user.id})
		if not contact_details_serliazer.is_valid():
			return api_utils.response(
					error=contact_details_serliazer.errors,
					code=status.HTTP_400_BAD_REQUEST)
		contact_details_params = contact_details_serliazer.validated_data
		email_id = contact_details_params.pop('email', None)
		with transaction.atomic():
			# Fetching contact if not available creating new one
			contact, created = Contact.objects.get_or_create(email=email_id, is_deleted=False)
			contact_details_params['contact'] = contact
			# Creating New Contact for user
			contact_details = ContactDetails.objects.create(**contact_details_params)
			# Creating Mapping Contact Details and User
			UserContactMapping.objects.create(
				user_id=request.user.id, contact_details_id=contact_details.id)
		response = {
			'status': True, 
			'contact_details': contact_details.id, 
			'message': "Sucessfully Added!"} 
		return api_utils.response(data=response)

	def put(self, request):
		"""Updating Contact Details"""
		params = copy.deepcopy(request.data)
		if not params.get('contact_details'):
			return api_utils.response(
					error='Contact Details is required',
					code=status.HTTP_400_BAD_REQUEST)
		user_contact_details = UserContactMapping.objects.filter(
				contact_details_id=params.get('contact_details'),
				is_deleted=False).select_related('contact_details').first()
		if not user_contact_details:
			return api_utils.response(
					error='Contact Details does not exists.',
					code=status.HTTP_400_BAD_REQUEST)
		# Checking object level permission whether the object belong to user or not
		self.check_object_permissions(request, user_contact_details)
		contact_details_serliazer = contacts_serializer.ContactDetailsSerializer(
			user_contact_details.contact_details,
			data=params,
			context={'user_id': request.user.id})
		if not contact_details_serliazer.is_valid():
			return api_utils.response(
					error=contact_details_serliazer.errors,
					code=status.HTTP_400_BAD_REQUEST)
		with transaction.atomic():
			# Updating the contact details
			contact_details_serliazer.save()
			if params.get('email'):
				contact, created = Contact.objects.get_or_create(
					email=params.get('email'), is_deleted=False)
				user_contact_details.contact_details.contact = contact
				user_contact_details.contact_details.save()
		
		response = {
			'status': True,
			'message': 'Sucessfully Update!'}
		return api_utils.response(data=response)

	def delete(self, request):
		"""Deleting Contact"""
		if not request.data.get('contact_details'):
			return api_utils.response(
				error='Contact Details is required!', code=status.HTTP_400_BAD_REQUEST)
		# Fetching contact detail to be deleted
		user_contact_details = UserContactMapping.objects.filter(
			contact_details_id=request.data.get('contact_details'), is_deleted=False)\
			.select_related('contact_details').first()
		if not user_contact_details:
			return api_utils.response(
				error='Contact does not exists.', 
				code=status.HTTP_400_BAD_REQUEST)
		# Checking object level permission 
		self.check_object_permissions(request, user_contact_details)

		# Deleting user contact
		with transaction.atomic():
			# Deleting contact Details
			contact_details = user_contact_details.contact_details
			contact_details.is_deleted = True
			contact_details.save()
			# Deleting User Contact Details mapping
			user_contact_details.is_deleted = True
			user_contact_details.save()
		return api_utils.response(
				data={'status': True, 'message': 'Sucessfully Deleted!'})

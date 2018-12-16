import re

from rest_framework import serializers

from contacts.models import *

class ContactDetailsSerializer(serializers.ModelSerializer):
	"""
	Validating Contact Details Request Params
	"""
	contact = serializers.IntegerField(required=False)
	email = serializers.CharField(max_length=255, required=False)

	def validate_email(self, data):
		"""
		Validating Email Pattern
		"""
		req = re.compile('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
		if data and not req.match(data):
			raise serializers.ValidationError('Please Provide Valid Email Id.')
		
		return data

	def validate_primary_mobile_number(self, data):
		"""Validating Mobile Number"""
		req = re.compile('(?!1)[6789]{1}[0-9]{9}')
		if data and not req.match(data):
			raise serializers.ValidationError('Please Provide Valid Primary Mobile Number.')
		return data

	def validate_secondary_mobile_number(self, data):
		"""Validating Mobile Number"""
		req = re.compile('(?!1)[6789]{1}[0-9]{9}')
		if data and not req.match(data):
			raise serializers.ValidationError('Please Provide Valid Secondary Mobile Number.')
		return data

	def validate(self, data):
		"""
		Validating Contact Details request and updating the contact id in that
		"""
		if not self.instance and not data.get('email'):
			raise serializers.ValidationError('Email Id is required!')

		if UserContactMapping.objects.filter(
				user_id=self.context.get('user_id'),
				contact_details__contact__email__iexact=data.get('email'),
				is_deleted=False).exists():
			raise serializers.ValidationError('Email Id already exists in you contact list.')

		return data

	class Meta:
		"""Model to Store Contact Details"""
		model = ContactDetails
		fields = '__all__'

class GetContactDetailsSerializer(serializers.ModelSerializer):
	"""
	Fetching User ContactDetails 
	"""
	email = serializers.SerializerMethodField(required=False)
	relationship = serializers.SerializerMethodField(required=False)

	def get_email(self, data):
		return data.contact.email

	def get_relationship(self, data):
		return data.relationship.name

	class Meta:
		model = ContactDetails
		fields = ('id', 'contact_id', 'email', 'name',
					'primary_mobile_number', 'secondary_mobile_number',
					'company_name', 'occupation', 'relationship', 'relationship_id',
					'address', 'landmark', 'city', 'pincode', 'state',)

class FetchContactDetailsSerializers(serializers.ModelSerializer):
	"""
	Fetching User Contact Details
	"""
	contact_details = GetContactDetailsSerializer()
	created_at = serializers.SerializerMethodField()

	def get_created_at(self, data):
		return data.created_at.strftime('%Y-%m-%d')

	class Meta:
		model = UserContactMapping
		fields = ('contact_details','created_at')

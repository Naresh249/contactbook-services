import pytest

from unittest import TestCase

from unittest.mock import Mock, patch
from client_authentication import utils as client_authentication_utils

pytestmark = pytest.mark.django_db

@pytest.mark.django_db
class TestGetAuthToken(TestCase):
	"""Test Case to get authtoken"""
	def test_get_auth_token(self):
		param = {
			'username': 'nky249@gmail.com',
			'password': 'naresh123'
		}
		patcher = patch('client_authentication.utils.get_authentication_token')
		get_auth_token = patcher.start()
		get_auth_token.return_value = {'status': True}
		response = client_authentication_utils.get_authentication_token(param)
		patcher.stop()
		self.assertEqual(response.get('status'), True)

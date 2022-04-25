import os
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password
 
class TryDjangoConfigTest(TestCase):
    """ Tests for config """
    def test_secret_key_strength(self):
        DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY') 
        try:
            is_strong = validate_password(DJANGO_SECRET_KEY)
        except Exception as e:
            msg = f" Weak password ->  {e.messages} "
            self.fail(e)


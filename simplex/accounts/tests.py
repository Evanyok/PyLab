from django.test import TestCase

from .models import TUser
from django.utils import timezone

class TUserTests(TestCase):
    def test_create_new_user(self):
        """
        create a new user
        """
        new_user = TUser(username="admin",password="1234",nickname="anick",email="admin@test.org",created=timezone.now())
        self.assertIs(new_user.deleted, False)
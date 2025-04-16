from typing import TYPE_CHECKING, cast
from django.test import TestCase
from django.contrib.auth import get_user_model

if TYPE_CHECKING:
    from ..models.users import CustomUser


class UserManagersTests(TestCase):
    def test_create_user(self):
        User = cast("CustomUser", get_user_model())
        user = User.objects.create_user(email="normal@user.com", password="foo")
        self.assertEqual(user.email, "normal@user.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = cast("CustomUser", get_user_model())
        admin_user = User.objects.create_superuser(
            email="super@user.com", password="foo"
        )
        self.assertEqual(admin_user.email, "super@user.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

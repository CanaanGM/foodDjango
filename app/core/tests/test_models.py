from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def __repr__(self):
        return super().__repr__()

    def test_create_user_with_email_sucess(self):
        """Testing if creating a user via email is successful"""
        email = "test@test.com"
        password = "supaPassword!"
        user = get_user_model().objects.create_user(email=email, password=password)

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = "test@TeSt.CoM"
        user = get_user_model().objects.create_user(email, "test")
        self.assertEqual(user.email, email.lower())

    def test_new_user_email_is_invalid(self):
        """Test creating a user with an empty email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test")

    def test_create_new_superuser(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser("test@test.com", "password")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

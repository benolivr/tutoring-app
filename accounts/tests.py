from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Classes

class CustomUserTests(TestCase):

    def setUp(self):
        self.class1 = Classes.objects.create(cSCI_Alphanumeric="CSCI 101", class_title="Introduction to Computer Science")
        self.class2 = Classes.objects.create(cSCI_Alphanumeric="CSCI 102", class_title="Data Structures")

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username='testuser',
            password='password123',
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            credit_standing='freshman'
        )
        user.tutoring_classes.set([self.class1, self.class2])
        user.save()

        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'Test')
        self.assertEqual(user.last_name, 'User')
        self.assertEqual(user.email, 'testuser@example.com')
        self.assertEqual(user.credit_standing, 'freshman')
        self.assertIn(self.class1, user.tutoring_classes.all())
        self.assertIn(self.class2, user.tutoring_classes.all())

    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username='adminuser',
            password='password123',
            first_name='Admin',
            last_name='User',
            email='adminuser@example.com',
            credit_standing='senior'
        )

        self.assertEqual(admin_user.username, 'adminuser')
        self.assertEqual(admin_user.first_name, 'Admin')
        self.assertEqual(admin_user.last_name, 'User')
        self.assertEqual(admin_user.email, 'adminuser@example.com')
        self.assertEqual(admin_user.credit_standing, 'senior')
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)
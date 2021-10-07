from django.test import TestCase
from .models import User, Profile, StartUp, StartUpMembers


# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.test_user_1 = User.objects.create(username='test_username', email='test@test.tst', is_admin=True,
                                               is_active=True)

    def test_is_staff(self):
        """
        check if is_staff property work fine
        :return: True
        """
        return self.assertTrue(self.test_user_1.is_staff)

    def test_username_field(self):
        """
        check if USERNAME_FIELD set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.USERNAME_FIELD, 'username')

    def test_username(self):
        """
        check if username set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.username, 'test_username')

    def test_email(self):
        """
        check if email set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.email, 'test@test.tst')

    def test_create(self):
        """
        check if your object create successfully
        :return: True
        """
        return self.assertIn(self.test_user_1, User.objects.all())

    def test_create_2(self):
        """
        check if object can created by manger
        :return: True
        """
        test_user_this = User.objects.create(username='test_username_2', email='test_email_2')
        return self.assertIn(test_user_this, User.objects.all())

    def test_create_3(self):
        user_test_3 = User(email='t@t.to', username='test_username_3')
        user_test_3.save()
        return self.assertIn(user_test_3, User.objects.all())

    def test_user_is_admin(self):
        """
        check if is_admin of object set correct
        :return: True
        """
        return self.assertTrue(self.test_user_1.is_admin)

    def test_user_is_active(self):
        """
        check if is_active of object set correct
        :return: True
        """
        return self.assertTrue(self.test_user_1.is_active)


class TestProfile(TestCase):
    def setUp(self):
        self.test_user_1 = User.objects.create(username='test_username',email='test@test.com')
        self.test_profile_1 = Profile.objects.create(user=self.test_user_1,first_name='test',last_name='testson')

    def testCreate(self):
        """
        check if profile object created and save in db
        :return: True
        """
        return self.assertIn(self.test_profile_1,Profile.objects.all())

    def testProfileUser(self):
        pass

    def testProfileFirstName(self):
        pass

    def testProfileLastName(self):
        pass

    def testProfileSoftDelete(self):
        pass

    def testProfileUndoSoftDelete(self):
        pass

    def testProfileCascade(self):
        pass


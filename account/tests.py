from django.test import TestCase
from .models import User, Profile, StartUp, StartUpMembers


# Create your tests here.

class TestUser(TestCase):
    def setUp(self):
        self.test_user_1 = User.objects.create(username='test_username', email='test@test.tst', is_superuser=True,
                                               is_active=True, is_staff=True)

    def testIs_staff(self):
        """
        check if is_staff property work fine
        :return: True
        """
        return self.assertTrue(self.test_user_1.is_staff)

    def testUsernameField(self):
        """
        check if USERNAME_FIELD set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.USERNAME_FIELD, 'username')

    def testUsername(self):
        """
        check if username set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.username, 'test_username')

    def testEmail(self):
        """
        check if email set correct
        :return: True
        """
        return self.assertEqual(self.test_user_1.email, 'test@test.tst')

    def testCreate(self):
        """
        check if your object create successfully
        :return: True
        """
        return self.assertIn(self.test_user_1, User.objects.all())

    def testCreate_2(self):
        """
        check if object can created by manger
        :return: True
        """
        test_user_this = User.objects.create(username='test_username_2', email='test_email_2')
        return self.assertIn(test_user_this, User.objects.all())

    def testCreate_3(self):
        user_test_3 = User(email='t@t.to', username='test_username_3')
        user_test_3.save()
        return self.assertIn(user_test_3, User.objects.all())

    def testUserIsAdmin(self):
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
        self.test_user_1 = User.objects.create(username='test_username', email='test@test.com')
        self.test_profile_1 = Profile.objects.create(user=self.test_user_1, first_name='firstname',
                                                     last_name='lastname')

    def testCreate(self):
        """
        check if profile object created and save in db
        :return: True
        """
        return self.assertIn(self.test_profile_1, Profile.objects.all())

    def testProfileUser(self):
        """
        check if user of Profile object set correct
        :return: True
        """
        return self.assertEqual(self.test_profile_1.user, self.test_user_1)

    def testProfileFirstName(self):
        """
        check if first name of profile user set true
        :return: True
        """
        return self.assertEqual(self.test_profile_1.first_name, 'firstname')

    def testProfileLastName(self):
        """
        check if last name of profile object set correct
        :return: True
        """
        return self.assertEqual(self.test_profile_1.last_name, 'lastname')

    def testUserRelatedName(self):
        """
        check if user related name user_of is correct Profile object
        :return: True
        """
        self.assertEqual(self.test_user_1.user_of, self.test_profile_1)

    def testStartUpRelatedName(self):
        """
        check if start up @property return correct start up
        :return: True
        """
        test_startup = StartUp.objects.create(header=self.test_profile_1,name='test_startup')
        test_user_2 = User.objects.create(username='test_username_2',email='test2@test.tst')
        test_profile_2 = Profile.objects.create(user=test_user_2,first_name='first_name',last_name='lastname')
        test_startup_memeber = StartUpMembers.objects.create(member=test_profile_2,startUp=test_startup,job_title='test developer')
        return self.assertEqual(test_profile_2.start_up,test_startup)

    def testProfileSoftDelete(self):
        """
        check if soft delete work for Profile user
        :return: True
        """
        self.test_profile_1.delete()
        return self.assertNotIn(self.test_profile_1, Profile.objects.all())

    def testProfileArchive(self):
        """
        check if soft deleted Profile object is still in Archive
        :return:
        """
        return self.assertIn(self.test_profile_1, Profile.objects.archive())

    def testProfileUndoSoftDelete(self):
        """
        check if soft delete und work fine
        :return: True
        """
        self.test_profile_1.deleted = False
        return self.assertIn(self.test_profile_1, Profile.objects.all())

    def testProfileCascade(self):
        """
        check if on delete of Profile object work correct
        :return: True
        """
        self.test_user_1.delete()
        return self.assertNotIn(self.test_profile_1, Profile.objects.all())


class TestStartUp(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='testusername', email='test@test.com')
        self.test_profile = Profile.objects.create(user=self.test_user, first_name='firstname', last_name='lastname')
        self.test_startup = StartUp.objects.create(header=self.test_profile, name='test_startup', website='test.co'
                                                   , description='a test startup')

    def testStartupCreate(self):
        """
        check if start up object created
        :return: True
        """
        self.assertIn(self.test_startup, StartUp.objects.all())

    def testStartUpHeader(self):
        """
        check if start up header of start up set correct
        :return: True
        """
        self.assertEqual(self.test_startup.header, self.test_profile)

    def testStartUpName(self):
        """
        check if start up name set correct
        :return: True
        """
        self.assertEqual(self.test_startup.name, 'test_startup')

    def testStartUpWebsite(self):
        """
        check if website of startup object set correct
        :return: True
        """
        return self.assertEqual(self.test_startup.website, 'test.co')

    def testStartUpDescription(self):
        """
        check if description of start up object set correct
        :return: True
        """
        return self.assertEqual(self.test_startup.description, 'a test startup')

    def testStartUpMembers(self):
        """
        check if member @property function return members
        :return: True
        """
        test_user_2 = User.objects.create(username='username_2', email='test2@test.tst')
        test_profile_2 = Profile.objects.create(user=test_user_2, first_name='fname2', last_name='lname2')
        StartUpMembers.objects.create(member=test_profile_2, startUp=self.test_startup, job_title='test engineer')
        return self.assertIn(test_profile_2, self.test_startup.members)


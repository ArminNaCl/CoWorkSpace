from django.test import TestCase
from .models import TestModel


class TestBaseModel(TestCase):
    def setUp(self):
        self.t1 = TestModel.objects.create()
        self.t2 = TestModel.objects.create()

    def testObjectCreate(self):
        """
        test if a object create and save in db
        :return: True
        """
        return self.assertIn(self.t1, TestModel.objects.all())

    def testObjectArchive(self):
        """
        test our manager after we make sure object is created
        :return: True
        """
        return self.assertIn(self.t1, TestModel.objects.archive())

    def testDeleteObject(self):
        """
        test if delete function is working
        :return: True
        """
        self.t2.delete()
        return self.assertTrue(self.t2.deleted)

    def testDeleteObjectManager(self):
        """
        test manager for deleted object
        :return: True
        """
        self.t2.delete()
        return self.assertNotIn(self.t2, TestModel.objects.all())

    def testDeleteArchive(self):
        """
        test manager(archive) for deleted object
        :return: True
        """
        return self.assertIn(self.t2, TestModel.objects.archive())

    def testHarDelete(self):
        """
        test hard delete
        :return: True
        """
        self.t2.hard_delete()
        return self.assert_(self.t2)

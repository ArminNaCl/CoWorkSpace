from django.test import TestCase
from django.utils import timezone
from account.models import User, Profile, StartUp
from building.models import Table, Room, Building
from .models import BookRoom, BookTable

import datetime


# Create your tests here.

class TestBookTable(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='test_username', email='email@test.tst')
        self.test_profile = Profile.objects.create(user=self.test_user, first_name='ftest', last_name='ltest')
        self.test_building = Building.objects.create(name='test_building', street='test_street', post_code='1234')
        self.test_table = Table.objects.create(building=self.test_building, capacity=1, price_per_day=40.000)
        start = timezone.now()
        end = start + timezone.timedelta(days=30)
        self.test_book = BookTable.objects.create(user=self.test_profile, table=self.test_table,
                                                  start_at=start, end_at=end)

    def testCreateObject(self):
        """
        check if booktable object created or not
        :return: True
        """
        return self.assertIn(self.test_book, BookTable.objects.all())

    def testArchiveObject(self):
        """
        check if book table model Archive Manger Work
        :return: True
        """
        return self.assertIn(self.test_book, BookTable.objects.archive())

    def testBookTableUser(self):
        """
        check if user of this BookTable object set correct
        :return: True
        """
        return self.assertEqual(self.test_book.user, self.test_profile)

    def testBookTableTable(self):
        """
        check if  table of this BookTable object set correct
        :return: True
        """
        return self.assertEqual(self.test_book.table, self.test_table)

    def testBookTableDays(self):
        """
        check if days property of this BookTable object calculate correct value
        :return: True
        """
        return self.assertEqual(self.test_book.days, 30)

    def testBookTablePrice(self):
        """
        check if price property of this BookTable object calculate correct value
        :return: True
        """
        return self.assertEqual(1200.00, self.test_book.price)


class TestBookRoom(TestCase):
    def setUp(self):
        self.test_user = User.objects.create(username='test_username', email='email@test.tst')
        self.test_profile = Profile.objects.create(user=self.test_user, first_name='ftest', last_name='ltest')
        self.test_startup = StartUp.objects.create(header=self.test_profile, name='test_startup')
        self.test_building = Building.objects.create(name='test_building', street='test_street', post_code='1234')
        self.test_room = self.test_building.room.create(capacity=8, has_tv=True, price_per_month=400.000)
        start = timezone.now()
        end = start + timezone.timedelta(6 * 30)
        self.test_book = BookRoom.objects.create(room=self.test_room, startUp=self.test_startup
                                                 , start_at=start, end_at=end)

    def testObjectCreate(self):
        """
        check if BookRoom object create or not
        :return: True
        """
        return self.assertIn(self.test_book, BookRoom.objects.all())

    def testBookRoomStartUp(self):
        """
        check if startup of this BookRoom object set correct
        :return: True
        """
        return self.assertEqual(self.test_book.startUp, self.test_startup)

    def testBookRoomRoom(self):
        """
        check if room of this BookRoom object set correct
        :return: True
        """
        return self.assertEqual(self.test_book.room, self.test_room)

    def testBookRoomMonths(self):
        """
        check if timestamps work right
        :return: True
        """
        return self.assertEqual(self.test_book.months, 6)

    def testBookRoomPrice(self):
        """
        check if price property of this BookRoom object return correct value
        :return: True
        """
        return self.assertEqual(self.test_book.price,2400.000)
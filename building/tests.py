from django.test import TestCase
from building.models import Building, Table, Room


class TestBuilding(TestCase):
    def setUp(self):
        self.test_building_1 = Building.objects.create(name='test_name', street='test_street', post_code='435')
        self.test_building_2 = Building.objects.create(name='test_name_2', street='test_street_2', post_code='126')
        self.test_building_3 = Building.objects.create(name='test_name_3', street='test_street_3', post_code='789')

    def testObjectCreate(self):
        """
        test if a object create and save in db
        :return: True
        """
        return self.assertIn(self.test_building_1, Building.objects.all())

    def testObjectArchive(self):
        """
        test our manager after we make sure object is created
        :return: True
        """
        return self.assertIn(self.test_building_1, Building.objects.archive())

    def testDeleteObject(self):
        """
        test if delete function is working
        :return: True
        """
        self.test_building_1.delete()
        return self.assertTrue(self.test_building_1.deleted)

    def testDeleteObjectManager(self):
        """
        test manager for deleted object
        :return: True
        """
        self.test_building_2.delete()
        return self.assertNotIn(self.test_building_2, Building.objects.all())

    def testDeleteArchive(self):
        """
        test manager(archive) for deleted object
        :return: True
        """
        return self.assertIn(self.test_building_2, Building.objects.archive())

    def testNameBuilding(self):
        """
        test name for  object
        :return: True
        """
        return self.assertEqual('test_name_3', self.test_building_3.name)

    def testStreetBuilding(self):
        """
        test street for building  object
        :return: True
        """
        return self.assertEqual('test_street_3', self.test_building_3.street)

    def testPostCodeBuilding(self):
        """
        test post code for building object
        :return: True
        """
        return self.assertEqual('789', self.test_building_3.post_code)


class TestTable(TestCase):
    def setUp(self):
        self.test_building_1 = Building.objects.create(name='test_name', street='test_street', post_code='435')
        self.test_table_1 = Table.objects.create(building=self.test_building_1, capacity=1, price_per_hour=15.000)
        self.test_table_2 = Table.objects.create(building=self.test_building_1, capacity=1, price_per_hour=15.000)

    def testObjectCreate(self):
        """
        test if a Table object create and save in db
        :return: True
        """
        return self.assertIn(self.test_table_1, Table.objects.all())

    def testTableInBuilding(self):
        """
        test if this table object is in building object
        :return: True
        """
        return self.assertIn(self.test_table_1, self.test_building_1.table.all())

    def testObjectArchive(self):
        """
        test our manager after we make sure Table object is created
        :return: True
        """
        return self.assertIn(self.test_table_1, Table.objects.archive())

    def testTableBuilding(self):
        """
        test if building of this table object is True
        :return: True
        """
        return self.assertEqual(self.test_table_1.building, self.test_building_1)

    def testTablesBuilding(self):
        """
        test if two table in same bilding
        :return: True
        """
        return self.assertEqual(self.test_table_1.building, self.test_table_2.building)

    def testTableCapacity(self):
        """
        test if Capacity of this table object set True
        :return: True
        """
        return self.assertEqual(self.test_table_1.capacity, 1)

    def testTablePrice(self):
        """
        test if Price per day of this table object set True
        :return: True
        """
        return self.assertEqual(self.test_table_1.price_per_day, 15.000)

    def testDeleteObject(self):
        """
        test if delete function is working
        :return: True
        """
        self.test_table_1.delete()
        return self.assertTrue(self.test_table_1.deleted)

    def testDeleteObjectManager(self):
        """
        test manager for deleted object
        :return: True
        """
        self.test_table_1.delete()
        return self.assertNotIn(self.test_table_1, Table.objects.all())

    def testCascadeBuilding(self):
        """
        test if delete a building delete tables
        :return: True
        """
        self.test_building_1.hard_delete()
        return self.assertNotIn(self.test_table_1, Table.objects.all())

    def testDeleteArchive(self):
        """
        test manager(archive) for deleted object
        :return: True
        """
        return self.assertIn(self.test_table_1, Table.objects.archive())


class TestRoom(TestCase):
    def setUp(self):
        self.test_building_1 = Building.objects.create(name='test_name', street='test_street', post_code='435')
        self.test_room_1 = Room.objects.create(building=self.test_building_1, capacity=6, price_per_day=90.000)
        self.test_room_2 = Room.objects.create(building=self.test_building_1, capacity=6, price_per_day=90.000,
                                               has_printer=True ,has_tv=True)

    def testObjectCreate(self):
        """
        test if a Room object create and save in db
        :return: True
        """
        return self.assertIn(self.test_room_1, Room.objects.all())

    def testRoomInBuilding(self):
        """
        test if this room object is in building object
        :return: True
        """
        return self.assertIn(self.test_room_1, self.test_building_1.room.all())

    def testObjectArchive(self):
        """
        test our manager after we make sure Room object is created
        :return: True
        """
        return self.assertIn(self.test_room_1, Room.objects.archive())

    def testRoomBuilding(self):
        """
        test if building of this room object is True
        :return: True
        """
        return self.assertEqual(self.test_room_1.building, self.test_building_1)

    def testRoomsBuilding(self):
        """
        test if two room in same building
        :return: True
        """
        return self.assertEqual(self.test_room_1.building, self.test_room_1.building)

    def testRoomCapacity(self):
        """
        test if Capacity of this room object set True
        :return: True
        """
        return self.assertEqual(self.test_room_2.capacity, 6)

    def testRoomPrice(self):
        """
        test if Price per month of this room object set True
        :return: True
        """
        return self.assertEqual(self.test_room_1.price_per_month, 90.000)

    def testRoomTV(self):
        """
        test if TV of this Room object set True
        :return: True
        """
        return self.assertFalse(self.test_room_1.has_tv)

    def testRoomTV2(self):
        """
        test if TV of this Room object set True
        :return: True
        """
        return self.assertTrue(self.test_room_2.has_tv)

    def testRoomPrinter(self):
        """
        test if Printer of this Room object set True
        :return: True
        """
        return self.assertFalse(self.test_room_1.has_printer)

    def testRoomPrinter2(self):
        """
        test if Printer of this Room object set True
        :return: True
        """
        return self.assertTrue(self.test_room_2.has_tv)

    def testDeleteObject(self):
        """
        test if delete function is working
        :return: True
        """
        self.test_room_1.delete()
        return self.assertTrue(self.test_room_1.deleted)

    def testDeleteObjectManager(self):
        """
        test manager for deleted object
        :return: True
        """
        self.test_room_1.delete()
        return self.assertNotIn(self.test_room_1, Room.objects.all())

    def testCascadeBuilding(self):
        """
        test if delete a building delete room
        :return: True
        """
        self.test_building_1.hard_delete()
        return self.assertNotIn(self.test_room_1, Room.objects.all())

    def testDeleteArchive(self):
        """
        test manager(archive) for deleted object
        :return: True
        """
        return self.assertIn(self.test_room_1, Room.objects.archive())




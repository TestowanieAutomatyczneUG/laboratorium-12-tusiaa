import unittest
from src.RandomUser import *

class TestsRandomUser(unittest.TestCase):
    def setUp(self):
        self.random_user = RandomUser("fea8be3e64777240")

    def test_init(self):
        self.assertIsNotNone(self.random_user)
    
    def test_get_info(self):
        self.assertIsInstance(self.random_user.get_info(), dict)
    
    def test_get_user(self):
        self.assertIsInstance(self.random_user.get_user(), dict)

    def test_get_gender(self):
        self.assertEqual(self.random_user.get_gender(), "male")

    def test_get_name(self):
        self.assertIsInstance(self.random_user.get_name(), dict)

    def test_get_title(self):
        self.assertEqual(self.random_user.get_title(), "Mr")

    def test_get_first_name(self):
        self.assertEqual(self.random_user.get_first_name(), "Brad")

    def test_get_last_name(self):
        self.assertEqual(self.random_user.get_last_name(), "Gibson")

    def test_get_location(self):
        self.assertIsInstance(self.random_user.get_location(), dict)

    def test_get_street(self):
        self.assertIn("name", self.random_user.get_street())

    def test_get_city(self):
        self.assertEqual(self.random_user.get_city(), "Kilcoole")

    def test_get_state(self):
        self.assertEqual(self.random_user.get_state(), "Waterford")

    def test_get_country(self):
        self.assertEqual(self.random_user.get_country(), "Ireland")

    def test_get_postcode(self):
        self.assertEqual(self.random_user.get_postcode(), 93027)

    def test_get_coordinates(self):
        self.assertIsInstance(self.random_user.get_coordinates(), dict)

    def test_get_timezone(self):
        self.assertIsInstance(self.random_user.get_timezone(), dict)

    def test_get_email(self):
        self.assertEqual(self.random_user.get_email(), "brad.gibson@example.com")

    def test_get_login(self):
        self.assertIsInstance(self.random_user.get_login(), dict)

    def test_get_uuid(self):
        self.assertEqual(self.random_user.get_uuid(), "155e77ee-ba6d-486f-95ce-0e0c0fb4b919")

    def test_get_username(self):
        self.assertEqual(self.random_user.get_username(), "silverswan131")

    def test_get_password(self):
        self.assertEqual(self.random_user.get_password(), "firewall")

    def test_get_dob(self):
        self.assertIn("date", self.random_user.get_dob())

    def test_get_registered(self):
        self.assertIn("date", self.random_user.get_registered())

    def test_get_phone(self):
        self.assertEqual(self.random_user.get_phone(), "011-962-7516")

    def test_get_cell(self):
        self.assertEqual(self.random_user.get_cell(), "081-454-0666")

    def test_get_id(self):
        self.assertIn("value", self.random_user.get_id())

    def test_get_picture(self):
        self.assertIsInstance(self.random_user.get_picture(), dict)

    def test_get_nat(self):
        self.assertEqual(self.random_user.get_nat(), "IE")
    
    def tearDown(self):
        del self.random_user

import unittest
import json
from unittest.mock import *
from src.RandomUser import *

class TestsRandomUser(unittest.TestCase):
    def setUp(self):
        f = open("data/Sample_JSON.json", "r")
        self.data = json.load(f)
        f.close()
        self.random_user = MagicMock()

    def test_init(self):
        self.assertIsNotNone(self.random_user)
    
    def test_get_info(self):
        self.random_user.get_info.return_value=self.data["info"]
        self.assertIsInstance(self.random_user.get_info(), dict)
    
    def test_get_user(self):
        self.random_user.get_user.return_value=self.data["results"][0]
        self.assertIsInstance(self.random_user.get_user(), dict)

    def test_get_gender(self):
        self.random_user.get_gender.return_value=self.data["results"][0]["gender"]
        self.assertEqual(self.random_user.get_gender(), "male")

    def test_get_name(self):
        self.random_user.get_name.return_value=self.data["results"][0]["name"]
        self.assertIsInstance(self.random_user.get_name(), dict)

    def test_get_title(self):
        self.random_user.get_title.return_value=self.data["results"][0]["name"]["title"]
        self.assertEqual(self.random_user.get_title(), "Mr")

    def test_get_first_name(self):
        self.random_user.get_first_name.return_value=self.data["results"][0]["name"]["first"]
        self.assertEqual(self.random_user.get_first_name(), "Brad")

    def test_get_last_name(self):
        self.random_user.get_last_name.return_value=self.data["results"][0]["name"]["last"]
        self.assertEqual(self.random_user.get_last_name(), "Gibson")

    def test_get_location(self):
        self.random_user.get_location.return_value=self.data["results"][0]["location"]
        self.assertIsInstance(self.random_user.get_location(), dict)

    def test_get_street(self):
        self.random_user.get_street.return_value=self.data["results"][0]["location"]["street"]
        self.assertIn("name", self.random_user.get_street())

    def test_get_city(self):
        self.random_user.get_city.return_value=self.data["results"][0]["location"]["city"]
        self.assertEqual(self.random_user.get_city(), "Kilcoole")

    def test_get_state(self):
        self.random_user.get_state.return_value=self.data["results"][0]["location"]["state"]
        self.assertEqual(self.random_user.get_state(), "Waterford")

    def test_get_country(self):
        self.random_user.get_country.return_value=self.data["results"][0]["location"]["country"]
        self.assertEqual(self.random_user.get_country(), "Ireland")

    def test_get_postcode(self):
        self.random_user.get_postcode.return_value=self.data["results"][0]["location"]["postcode"]
        self.assertEqual(self.random_user.get_postcode(), 93027)

    def test_get_coordinates(self):
        self.random_user.get_coordinates.return_value=self.data["results"][0]["location"]["coordinates"]
        self.assertIsInstance(self.random_user.get_coordinates(), dict)

    def test_get_timezone(self):
        self.random_user.get_timezone.return_value=self.data["results"][0]["location"]["timezone"]
        self.assertIsInstance(self.random_user.get_timezone(), dict)

    def test_get_email(self):
        self.random_user.get_email.return_value=self.data["results"][0]["email"]
        self.assertEqual(self.random_user.get_email(), "brad.gibson@example.com")

    def test_get_login(self):
        self.random_user.get_login.return_value=self.data["results"][0]["login"]
        self.assertIsInstance(self.random_user.get_login(), dict)

    def test_get_uuid(self):
        self.random_user.get_uuid.return_value=self.data["results"][0]["login"]["uuid"]
        self.assertEqual(self.random_user.get_uuid(), "155e77ee-ba6d-486f-95ce-0e0c0fb4b919")

    def test_get_username(self):
        self.random_user.get_username.return_value=self.data["results"][0]["login"]["username"]
        self.assertEqual(self.random_user.get_username(), "silverswan131")

    def test_get_password(self):
        self.random_user.get_password.return_value=self.data["results"][0]["login"]["password"]
        self.assertEqual(self.random_user.get_password(), "firewall")

    def test_get_dob(self):
        self.random_user.get_dob.return_value=self.data["results"][0]["dob"]
        self.assertIn("date", self.random_user.get_dob())

    def test_get_registered(self):
        self.random_user.get_registered.return_value=self.data["results"][0]["registered"]
        self.assertIn("date", self.random_user.get_registered())

    def test_get_phone(self):
        self.random_user.get_phone.return_value=self.data["results"][0]["phone"]
        self.assertEqual(self.random_user.get_phone(), "011-962-7516")

    def test_get_cell(self):
        self.random_user.get_cell.return_value=self.data["results"][0]["cell"]
        self.assertEqual(self.random_user.get_cell(), "081-454-0666")

    def test_get_id(self):
        self.random_user.get_id.return_value=self.data["results"][0]["id"]
        self.assertIn("value", self.random_user.get_id())

    def test_get_picture(self):
        self.random_user.get_picture.return_value=self.data["results"][0]["picture"]
        self.assertIsInstance(self.random_user.get_picture(), dict)

    def test_get_nat(self):
        self.random_user.get_nat.return_value=self.data["results"][0]["nat"]
        self.assertEqual(self.random_user.get_nat(), "IE")
    
    def tearDown(self):
        return super().tearDown()

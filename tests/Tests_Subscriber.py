import unittest
from unittest.mock import *
from parameterized import parameterized
from src.Subscriber import *

class TestsSubscriber(unittest.TestCase):
    def setUp(self):
        self.subscriber = Subscriber()

    def test_init(self):
        self.assertIsNotNone(self.subscriber)

    @patch('src.Client.Client', spec=Client)
    def test_add_client(self, mock_client):
        self.subscriber.add_client(mock_client)
        self.assertIn(mock_client, self.subscriber.clients)

    @patch('src.Client.Client', spec=Client)
    def test_remove_client(self, mock_client):
        self.subscriber.add_client(mock_client)
        self.subscriber.remove_client(mock_client)
        self.assertNotIn(mock_client, self.subscriber.clients)

    @patch('src.Client.Client', spec=Client)
    def test_send_message(self, mock_client):
        self.subscriber.add_client(mock_client)
        self.subscriber.send_message(mock_client, "message")
        mock_client.receive_message.assert_called_with("message")

    @parameterized.expand([
        ("client", ValueError),
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_add_client_invalid_arguments(self, client, exception):
        with self.assertRaises(exception):
            self.subscriber.add_client(client)

    @parameterized.expand([
        ("client", ValueError),
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    def test_remove_client_invalid_arguments(self, client, exception):
        with self.assertRaises(exception):
            self.subscriber.remove_client(client)

    @parameterized.expand([
        ("client", "message", ValueError),
        ("", "message", ValueError),
        (5, "message", ValueError),
        (5.5, "message", ValueError),
        (True, "message", ValueError),
        (None, "message", ValueError),
        ([1,2,3], "message", ValueError),
        ({'name': 2, 'grades': 4}, "message", ValueError),
        ("client", "", ValueError),
        ("client", 5, ValueError),
        ("client", 5.5, ValueError),
        ("client", True, ValueError),
        ("client", None, ValueError),
        ("client", [1,2,3], ValueError),
        ("client", {'name': 2, 'grades': 4}, ValueError),
    ])
    @patch.object(Client, 'receive_message', return_value=ValueError)
    def test_send_message_invalid_arguments(self, client, message, exception, mock_receive_message):
        with self.assertRaises(exception):
            self.subscriber.send_message(client, message)

    def tearDown(self):
        del self.subscriber
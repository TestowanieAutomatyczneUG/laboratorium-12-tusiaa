import unittest
from unittest.mock import *
from parameterized import parameterized
from src.Messenger import *

class TestsMessenger(unittest.TestCase):

    @patch('src.TemplateEngine.TemplateEngine', spec=TemplateEngine)
    @patch('src.MailServer.MailServer', spec=MailServer)
    def setUp(self, mock_mail_server, mock_template_engine):
        self.mail_server = mock_mail_server
        self.template_engine = mock_template_engine
        self.messenger = Messenger(mock_mail_server, mock_template_engine)

    def test_init(self):
        self.assertIsNotNone(self.messenger)
    
    @patch('src.Client.Client', spec=Client)
    def test_send_message_mail_server(self, mock_client):
        self.messenger.send_message(mock_client, "message")
        self.mail_server.send_message.assert_called_with(mock_client, self.template_engine.message("message"))

    @patch('src.Client.Client', spec=Client)
    def test_send_message_template_engine(self, mock_client):
        self.messenger.send_message(mock_client, "message")
        self.template_engine.message.assert_called_with("message")

    @patch('src.Client.Client', spec=Client)
    def test_receive_message(self, mock_client):
        self.messenger.receive_message(mock_client, "message")
        self.mail_server.receive_message.assert_called_with(mock_client, "message")

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
    @patch('src.MailServer.MailServer', spec=MailServer)
    def test_init_wrong_template_engine(self, template_engine, exception, mock_mail_server):
        with self.assertRaises(exception):
            Messenger(mock_mail_server, template_engine)

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
    @patch('src.TemplateEngine.TemplateEngine', spec=TemplateEngine)
    def test_init_wrong_mail_server(self, mail_server, exception, mock_template_engine):
        with self.assertRaises(exception):
            Messenger(mail_server, mock_template_engine)

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
    def test_send_message_wrong_client(self, client, exception):
        with self.assertRaises(exception):
            self.messenger.send_message(client, "message")

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    @patch('src.Client.Client', spec=Client)
    def test_send_message_wrong_message(self, message, exception, mock_client):
        with self.assertRaises(exception):
            self.messenger.send_message(mock_client, message)

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
    def test_receive_message_wrong_client(self, client, exception):
        with self.assertRaises(exception):
            self.messenger.receive_message(client, "message")

    @parameterized.expand([
        ("", ValueError),
        (5, ValueError),
        (5.5, ValueError),
        (True, ValueError),
        (None, ValueError),
        ([1,2,3], ValueError),
        ({'name': 2, 'grades': 4}, ValueError),
    ])
    @patch('src.Client.Client', spec=Client)
    def test_receive_message_wrong_message(self, message, exception, mock_client):
        with self.assertRaises(exception):
            self.messenger.receive_message(mock_client, message)

from src.TemplateEngine import TemplateEngine
from src.MailServer import MailServer
from src.Client import Client

class Messenger:
    def __init__(self, mail_server: MailServer, template_engine: TemplateEngine):
        if not isinstance(mail_server, MailServer):
            raise ValueError("mail_server must be an instance of MailServer")
        if not isinstance(template_engine, TemplateEngine):
            raise ValueError("template_engine must be an instance of TemplateEngine")
        self.mail_server = mail_server
        self.template_engine = template_engine

    def send_message(self, client: Client, message: str):
        if not isinstance(client, Client):
            raise ValueError("client must be an instance of Client")
        if not isinstance(message, str) or len(message) == 0:
            raise ValueError("message must be an instance of str")
        self.mail_server.send_message(client, self.template_engine.message(message))

    def receive_message(self, client: Client, message: str):
        if not isinstance(client, Client):
            raise ValueError("client must be an instance of Client")
        if not isinstance(message, str) or len(message) == 0:
            raise ValueError("message must be an instance of str")
        self.mail_server.receive_message(client, message)

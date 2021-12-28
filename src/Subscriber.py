from src.Client import Client

class Subscriber:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        if not isinstance(client, Client) or client in self.clients:
            raise ValueError("Invalid client")
        self.clients.append(client)

    def remove_client(self, client):
        if not isinstance(client, Client) or client not in self.clients:
            raise ValueError("Invalid client")
        self.clients.remove(client)

    def send_message(self, client, message):
        if not isinstance(client, Client) or client not in self.clients:
            raise ValueError("Invalid client")
        client.receive_message(message)
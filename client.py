import socket

class client:
    def __init__(self, client_name):
        self.name = client_name
        self.client = None

    def connect(self, addr):
        if addr == None:
            return
        
        print(f"Attempting to connect to server on address {addr}")
        self.client = socket.create_connection(address=addr)
        

    def send_packet(self, data):
        self.client.send(data)

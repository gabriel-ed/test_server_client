import socket

class server:
    def __init__(self, host, port):
        if host is None and port is None:
            self.host = '127.0.0.1'
            self.port = 8000     
        else:
            self.host = host
            self.port = port
            
        self.server_socket = None

    def start(self):
        self.server_socket = socket.create_server(address=(self.host, self.port), family=socket.AF_INET)
        print(f"Listening on {self.host}:{self.port}")

        while True:
            client_socket, client_address = self.server_socket.accept()
            print(f"Connection from {client_address}")

            with client_socket:
                while True:
                    data = client_socket.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")

                    # handle response.

    def stop(self):
        self.server_socket.close()
        print(f"Closed socket.")
    
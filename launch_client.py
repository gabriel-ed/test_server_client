import client

import threading

def main():
    print(f"Launching Client Gus...")

    my_client = client.client(client_name="Gus")

    my_client.connect(('127.0.0.1',8000))
    
    my_client.send_packet(data=b"Hello from Client.")

if __name__ == "__main__":
    main()
import server

import threading

def main():
    print(f"Launching Server...")
    host = '127.0.0.1'
    port = 8000
    my_server = server.server(host=host, port=port)

    my_server.start()
    
    my_server.stop()
if __name__ == "__main__":
    main()
from socket import *

def create_tcp_socket():
    try:
        serverSocket = socket(AF_INET, SOCK_STREAM)
        return serverSocket
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None


def bind_socket(server_socket, port):
    try:
        server_socket.bind(('', port))
        print(f"Server bound to port {port}")
        return True
    except socket.error as e:
        print(f"Error binding to port {port}: {e}")
        return False


def setup_listener(server_socket, backlog=5):
    try:
        server_socket.listen(backlog)
        print(f"Server is listening for connections (backlog: {backlog})")
        return True
    except socket.error as e:
        print(f"Error setting up listener: {e}")
        return False


def handle_client(connection_socket, client_address):
    try:
        print(f"Connected to client: {client_address}")
        
        # Receive data
        message = connection_socket.recv(1024).decode()
        print(f"Received from client: '{message}'")
        
        # Echo it back
        connection_socket.send(message.encode())
        print(f"Echoed back: '{message}'")
        
    except socket.error as e:
        print(f"Error handling client: {e}")
    finally:
        connection_socket.close()
        print(f"Connection closed with {client_address}")


def run_server(server_socket):
    print("Server is ready to accept connections...")
    
    try:
        while True:
            connectionSocket, clientAddress = server_socket.accept()            
            handle_client(connectionSocket, clientAddress)
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except socket.error as e:
        print(f"Socket error: {e}")


def main():
    serverPort = 12000
    
    serverSocket = create_tcp_socket()
    if serverSocket is None:
        print("Failed to create socket. Exiting.")
        return
    
    if not bind_socket(serverSocket, serverPort):
        print("Failed to bind to port. Exiting.")
        serverSocket.close()
        return
    
    if not setup_listener(serverSocket):
        print("Failed to set up listener. Exiting.")
        serverSocket.close()
        return
    
    run_server(serverSocket)
    
    serverSocket.close()
    print("Server closed.")


if __name__ == "__main__":
    main()

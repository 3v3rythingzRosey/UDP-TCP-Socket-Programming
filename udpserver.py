from socket import *


def create_udp_socket():
    try:
        serverSocket = socket(AF_INET, SOCK_DGRAM)
        return serverSocket
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None


def bind_socket(server_socket, port):
    try:
        server_socket.bind(('', port))
        print(f"Server is listening on port {port}")
        return True
    except socket.error as e:
        print(f"Error binding to port {port}: {e}")
        return False


def check_even_odd(number_str):
    try:
        number = int(number_str)
        if number % 2 == 0:
            return "even"
        else:
            return "odd"
    except ValueError:
        return "Error: Invalid number"


def run_server(server_socket):
    print("Server is ready to receive...")
    
    try:
        while True:
            data, client_address = server_socket.recvfrom(2048)
            number_str = data.decode()
            print(f"Received '{number_str}' from {client_address}")
            response = check_even_odd(number_str)
            print(f"Sending response: '{response}'")
            server_socket.sendto(response.encode(), client_address)
            
    except KeyboardInterrupt:
        print("\nServer shutting down...")
    except socket.error as e:
        print(f"Socket error: {e}")


def main():
    serverPort = 12000
    serverSocket = create_udp_socket()
    if serverSocket is None:
        print("Failed to create socket. Exiting.")
        return
    
    if not bind_socket(serverSocket, serverPort):
        print("Failed to bind to port. Exiting.")
        serverSocket.close()
        return
    
    run_server(serverSocket)
    
    serverSocket.close()
    print("Server closed.")


if __name__ == "__main__":
    main()

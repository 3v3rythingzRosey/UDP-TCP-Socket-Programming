from socket import *


def create_tcp_socket():
    try:
        clientSocket = socket(AF_INET, SOCK_STREAM)
        return clientSocket
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None


def connect_to_server(client_socket, server_name, server_port):
    try:
        client_socket.connect((server_name, server_port))
        print(f"Connected to server {server_name}:{server_port}")
        return True
    except socket.error as e:
        print(f"Error connecting to server: {e}")
        return False


def get_message_input():
    message = input("Enter message to echo: ")
    return message


def send_message(client_socket, message):
    try:
        client_socket.send(message.encode())
        print(f"Sent to server: '{message}'")
        return True
    except socket.error as e:
        print(f"Error sending data: {e}")
        return False


def receive_response(client_socket):
    try:
        data = client_socket.recv(1024)
        if data:
            return data.decode()
        else:
            print("Server closed the connection")
            return None
    except socket.error as e:
        print(f"Error receiving data: {e}")
        return None


def main():
    serverName = '192.168.56.106'  # Change to your server IP
    serverPort = 12000
    
    clientSocket = create_tcp_socket()
    if clientSocket is None:
        print("Failed to create socket. Exiting.")
        return
    
    if not connect_to_server(clientSocket, serverName, serverPort):
        print("Failed to connect to server. Exiting.")
        clientSocket.close()
        return
    
    message = get_message_input()
    
    if not send_message(clientSocket, message):
        print("Failed to send message. Exiting.")
        clientSocket.close()
        return
    
    response = receive_response(clientSocket)
    if response:
        print(f"Echo from server: '{response}'")
    else:
        print("Failed to receive response")
    
    clientSocket.close()
    print("Connection closed")


if __name__ == "__main__":
    main()
#Client program to send a number to server for processing & recieving feedback whether odd or even
from socket import *


def create_udp_socket():
    try:
        clientSocket = socket(AF_INET,SOCK_DGRAM)
        return clientSocket
    except socket.error as e:
        print(f"Error creating socket: {e}")
        return None
        
def get_number_input():
    while True:
        user_input = input("Enter a number: ")
        try:
            int(user_input)
            return user_input
        except ValueError:
            print("Invalid input, please try again with a VALID number")

def send_number(client_socket, number, server_name, server_port):
    try:
        message = number.encode()
        print(f"Sending number {number} to {server_name}:{server_port}...")
        client_socket.sendto(message, (server_name, server_port))
        return True
    except socket.error as e:
        print(f"Error sending data: {e}")
        return False
        
def receive_response(client_socket):
    try:
        client_socket.settimeout(10)
        data, server_address = client_socket.recvfrom(2048)
        return data.decode()
    except TimeoutError: 
        print("Server did not respond in time (10 seconds timeout reached)")
        return None
    except socket.error as e:
        print(f"Error receiving data: {e}")
        return None

def main():
    serverName ='192.168.56.106' 
    serverPort = 12000

    clientSocket = create_udp_socket()
    if clientSocket is None:
        return

    number = get_number_input()
    if not number:
        clientSocket.close()
        return

    if not send_number(clientSocket, number, serverName, serverPort):
        print("Failed to send data. Exiting.")
        clientSocket.close()
        return

    response = receive_response(clientSocket)
    if response:
        print(f"\n✅ Server response: {response}")
    else:
        print("\n Failed to receive response from server")

    clientSocket.close()
    print("Connection closed")

if __name__ == "__main__":
    main()

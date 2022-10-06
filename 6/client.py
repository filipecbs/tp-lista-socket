from socket import *

SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

while True:
	message = input()
	client_socket.send(message.encode())
	response = client_socket.recv(1024).decode()
	print(response)

	if "Até logo!" in response:
		break

client_socket.close()

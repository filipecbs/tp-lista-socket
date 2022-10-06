from socket import *
SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))
i = 1
number = int(input('Input number:'))

while i <= number:
	num = str(i) + " "
	client_socket.send(num.encode())
	i += 1
client_socket.close()

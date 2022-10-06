from socket import *
SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
number = int(input('Input number:'))
i = 1

while i <= number:
	num = str(i) + " "
	client_socket.sendto(num.encode(),(SERVER_NAME, SERVER_PORT))
	i += 1
client_socket.close()

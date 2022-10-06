from socket import *
SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_DGRAM)
while True:
	message = input('Input lowercase sentence:')
	if message == '':
		break
	client_socket.sendto(message.encode(),(SERVER_NAME, SERVER_PORT))
	modified_message, server_address = client_socket.recvfrom(2048)
	msg_decoded = modified_message.decode()
	print(modified_message.decode())
client_socket.close()

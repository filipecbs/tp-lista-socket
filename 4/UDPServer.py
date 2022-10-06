from socket import *
import threading

def upper_sentence(srv_sock, msg, cli_addr):
	num = msg.decode()
	if not num:
		srv_sock.close()
		return
	print(num)

SERVER_PORT = 12000
server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind(('', SERVER_PORT))
print('The server is ready to receive')
while True:
	message, client_address = server_socket.recvfrom(2048)
	client = threading.Thread(target=upper_sentence, args=(server_socket, message, client_address))
	client.start()

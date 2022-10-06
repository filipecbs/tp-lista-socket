from socket import *
SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(5)
print('The server is ready to receive')
connection_socket, addr = SERVER_SOCKET.accept()
while True:
	sentence = connection_socket.recv(1024).decode()
	capitalized_sentence = sentence.upper()
	connection_socket.send(capitalized_sentence.encode())
	if capitalized_sentence == '':
		break
connection_socket.close()

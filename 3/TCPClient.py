from socket import *
SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))
while True:
	sentence = input('Input lowercase sentence:')
	if len(sentence) == 0:
		break
	client_socket.send(sentence.encode())
	modified_sentence = client_socket.recv(1024)
	msg_decoded = modified_sentence.decode()
	print('From Server: ', modified_sentence.decode())
client_socket.close()

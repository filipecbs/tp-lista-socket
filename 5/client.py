from socket import *
import json

SERVER_NAME = ''
SERVER_PORT = 12000
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect((SERVER_NAME, SERVER_PORT))

while True:
	login = {}
	login['username'] = input('Username: ')
	login['password'] = input('Password: ')
	client_socket.send(json.dumps(login).encode())
	response = client_socket.recv(1024).decode()
	if login['username'] == '' or login['password'] == '':
		client_socket.close()
		break
	if response == 'Login successful':
		print(response)
		break
	else:
		print(response)

client_socket.close()

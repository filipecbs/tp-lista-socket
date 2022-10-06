from socket import *
import threading
import json

def log(conn_soc, cli_addr):
	while True:
		login = json.loads(conn_soc.recv(1024).decode())
		if login['username'] == 'admin' and login['password'] == 'admin':
			conn_soc.send('Login successful'.encode())
			break
		elif login['username'] == '' or login['password'] == '':
			conn_soc.close()
			return

		else:
			conn_soc.send('Login failed'.encode())

SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(1)
print('The server is ready to receive')

while True:
	client = threading.Thread(target=log, args=SERVER_SOCKET.accept())
	client.start()

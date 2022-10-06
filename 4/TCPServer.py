from socket import *
import threading

def upper_sentence(conn_soc, cli_addr):
	while True:
		num = conn_soc.recv(1024).decode()
		if not num:
			conn_soc.close()
			return
		print(num)

SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(1)
print('The server is ready to receive')

while True:
	client = threading.Thread(target=upper_sentence, args=SERVER_SOCKET.accept())
	client.start()

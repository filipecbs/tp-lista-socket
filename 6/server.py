from socket import *
import threading

def recv_msg(conn_soc, cli_addr):
	start = conn_soc.recv(1024)
	conn_soc.send("Olá! Bem-vindo! Qual o seu nome?".encode())
	username = conn_soc.recv(1024)

	options_string = f"Certo, {username.decode()}! Como posso te ajudar? Digite o numero que corresponde a opção desejada:\n1. Agendar um horario de monitoria\n2. Listar as proximas atividades da disciplina\n3. E-mail do professor"
	conn_soc.send(options_string.encode())

	msg = conn_soc.recv(1024)
	end_msg = "Obrigado por utilizar nossos serviços!\nAté logo!"
	option = msg.decode()

	if option == '1':
		conn_soc.send(f"Para agendar uma monitoria, basta enviar um e-mail para cainafigueiredo@poli.ufrj.br \n{end_msg}".encode())
	elif option == '2':
		atividades = "P1: 26 de Maio de 2022\nLista3: 29 de Maio de 2022"
		conn_soc.send(f"Fique atento para as datas das proximas atividades. Confira o que vem por aí!\n{atividades}\n{end_msg}".encode())
	elif option == '3':
		conn_soc.send(f"Quer falar com o professor? o e-mail dele eh sadoc@dcc.ufrj.br \n{end_msg}".encode())
	else:
		conn_soc.send(end_msg.encode())

SERVER_PORT = 12000
SERVER_SOCKET = socket(AF_INET, SOCK_STREAM)
SERVER_SOCKET.bind(('', SERVER_PORT))
SERVER_SOCKET.listen(1)
print('The server is ready to receive')

while True:
	client = threading.Thread(target=recv_msg, args=SERVER_SOCKET.accept())
	client.start()

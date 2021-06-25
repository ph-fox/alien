import socket, readline, os

ip = '10.9.1.23'
port = 6663

def connection():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	print('connected successfully!')

	while True:
		cmd = input('~# ')
		if cmd == 'gg':
			s.send('gg'.encode())
			print(s.recv(1024).decode())
		elif s.recv(1024).decode() == 'tar':
			ui = input('enter url: ')
			s.send(ui.decode())
		elif cmd == 'clear':
			os.system('clear')
		else:
			s.send(cmd.encode())
			print(s.recv(1024).decode())

connection()

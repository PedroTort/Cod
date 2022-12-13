import socket as sk
import tkinter as tk


class Client:
    def __init__(self):
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.host_ip = ''
        self.port = ''
        self.client = False
        self.msg = ''

    
    # def client_connection(self):
    #     print('cliente')
    #     print(self.client)
    #     print(self.host_ip)
    #     print(self.port)
    #     with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    #         s.connect((self.host_ip, self.port))
    #         s.send(self.msg.encode())
    #         data = s.recv(1024)
    #         print(data)
    #         self.client= True
    #     # print(f"Received {data!r}")

    def connect(self):
        self.socket.connect((self.host_ip,self.port))
        # self.socket.sendall(b"data")
        self.client= True

    def send_msg(self, msg):
        # self.socket.send(self.msg.encode())
        import time
        time.sleep(1)
        self.socket.sendall(str(msg).encode())




    # # fazendo a conexão
    # def connect(self):
    #     #connect() cria o socket obj, pra fazer a conexão com o servidor
    #     #sendall() é usado pra mandar as mensagens, e o recv() lê.
    #     self.socket.connect(self.host_ip,self.port)

    # # criando a conexão
    # def create_connection(self):
    #     #bind() associando o socket com a rede e a porta
    #     self.socket.bind(self.host_ip,self.port) 
    #     #listen() permite que o servidor receba conexões

    #     #accept() bloqueia execuções e espera por uma conexão vindo
    #     self.teste, self.host_ip = self.socket.accept() 


    def get_ipv4(self):
        #AF_INET eh o ipv4, SOCK_DGRAM eh o tipo do socket
        s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM) 
        s.settimeout(0)
        try:
            # doesn't even have to be reachable
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

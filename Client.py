import socket as sk
import tkinter as tk


class Client:
    def __init__(self):
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.host_ip = ''
        self.port = ''
        self.client = False
        self.msg = ''

    def connect(self):
        #connect() cria o socket obj, pra fazer a conexão com o servidor
        self.socket.connect((self.host_ip,self.port))
        self.client= True

    def send_msg(self, msg):
        import time
        time.sleep(1)
        #sendall() é usado pra mandar as mensagens, e o recv() lê.
        self.socket.sendall(str(msg).encode())

    def get_ipv4(self):
        #AF_INET eh o ipv4, SOCK_DGRAM eh o tipo do socket
        s = sk.socket(sk.AF_INET, sk.SOCK_DGRAM) 
        s.settimeout(0)
        try:
            s.connect(('10.254.254.254', 1))
            IP = s.getsockname()[0]
        except Exception:
            IP = '127.0.0.1'
        finally:
            s.close()
        return IP

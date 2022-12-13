import socket as sk


class Server():
    def __init__(self):
        self.socket = sk.socket(sk.AF_INET, sk.SOCK_STREAM)
        self.host_ip = ''
        self.port = ''
        self.server = False
        self.msg = ''
        self.connection = ''
        self.address = ''

    def create_server_connection(self):
        #bind() associando o socket com a rede e a porta
        self.socket.bind((self.host_ip, self.port))
        #listen() permite que o servidor receba conexões
        self.socket.listen(2)
        #accept() bloqueia execuções e espera por uma conexão vindo
        self.connection, self.address = self.socket.accept()
        self.server = True
    
    def recieve_message(self):
        with self.connection:
            msg = self.connection.recv(1024).decode()
            return msg

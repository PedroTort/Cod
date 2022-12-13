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


    # def server_connection(self):
    #     print('servidor')
    #     print(self.host_ip)
    #     print(self.port)
    #     with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
    #         s.bind((self.host_ip, self.port))
    #         s.listen()
    #         conn, addr = s.accept()
    #         with conn:
    #             print(f"Connected by {addr}")
    #             while True:
    #                 data = conn.recv(1024).decode()
    #                 self.server = True
    #                 if not data:
    #                     break
    #                 conn.sendall(data)
    #                 print(data)

    def create_server_connection(self):
        self.socket.bind((self.host_ip, self.port))
        self.socket.listen(2)
        self.connection, self.address = self.socket.accept()
        self.server = True
    
    def connect(self):
        with self.connection:
            print("a")
            # while self.msg:
            #     self.msg = self.connection.recv(1024)
            #     self.server = True
            #     if not self.msg:
            #         break
            #     self.connection.sendall(self.msg)
    
    def recieve_message(self):
        with self.connection:
            msg = self.connection.recv(1024)
            return msg

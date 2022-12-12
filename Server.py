import socket as sk


class Server():
    def __init__(self):
        self.host_ip = ''
        self.port = ''


    def server_connection(self):
        print('servidor')
        print(self.host_ip)
        print(self.port)
        with sk.socket(sk.AF_INET, sk.SOCK_STREAM) as s:
            s.bind((self.host_ip, self.port))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    conn.sendall(data)


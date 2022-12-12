import tkinter as tk

from Client import *
from Server import *


class ConnectionInterface:
    def __init__(self):
        # build ui
        
        toplevel1 = tk.Tk()
        toplevel1.configure(
            background="#eabdd5",
            cursor="based_arrow_up",
            height=200,
            width=320)
        toplevel1.geometry("320x200")

        self.ip = tk.StringVar()
        self.port = tk.StringVar()

        self.con = Client()

        self.serv = Server()

        # self.host = tk.BooleanVar()
        # self.client = tk.BooleanVar()

        # toplevel1.maxsize(480, 640)
        # toplevel1.minsize(480, 640)
        self.id_label = tk.Label(toplevel1)
        self.id_label.configure(text='ID:')
        self.id_label.place(anchor="nw", x=50, y=50)

        self.port_label = tk.Label(toplevel1)
        self.port_label.configure(text='Porta:')
        self.port_label.place(anchor="nw", x=50, y=75)

        self.port_entry = tk.Entry(toplevel1, textvariable=self.port)
        self.port_entry.place(anchor="nw", x=120, y=75)

        self.id_entry = tk.Entry(toplevel1)
        self.id_entry.place(anchor="nw", x=120, y=50)
        

        self.create_session_button = tk.Button(toplevel1, command=self.make_server_connection)
        # self.create_session_button.configure(text='Criar Sessao')
        self.create_session_button.configure(text='Servidor')
        self.create_session_button.place(anchor="nw", x=100, y=100)

        self.connect_button = tk.Button(toplevel1, command=self.make_client_connection)
        # self.connect_button.configure(text='Conectar')
        self.connect_button.configure(text='Cliente')
        self.connect_button.place(anchor="nw", x=200, y=100)

        self.connect_button = tk.Button(toplevel1, command=self.get_ip_function)
        self.connect_button.configure(text='Get Ip')
        self.connect_button.place(anchor="nw", x=150, y=150)
        
        self.title_label = tk.Label(toplevel1)
        self.title_label.configure(text='8B6T')
        self.title_label.place(anchor="n", x=160, y=10)

        toplevel1.pack_propagate(0)

        # Main widget
        self.mainwindow = toplevel1

        # Obj connection
        
    def run(self):
        self.mainwindow.mainloop()

    def get_ip_function(self):
        self.ip.set(self.con.get_ipv4())
        self.id_entry.config(textvariable=self.ip,state="readonly")

    def make_client_connection(self):
        self.con.host_ip = self.con.get_ipv4()                
        self.con.port = int(self.port.get())
        self.con.client_connection()

    def make_server_connection(self):
        self.serv.host_ip = self.con.get_ipv4()           
        self.serv.port = int(self.port.get())
        self.serv.server_connection()




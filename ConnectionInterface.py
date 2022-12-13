import tkinter as tk

from Client import *
from MessageWindow import *
from Server import *


class ConnectionInterface:
    def __init__(self):
        # build ui
        
        self.toplevel1 = tk.Tk()
        self.toplevel1.configure(
            background="#eabdd5",
            cursor="based_arrow_up",
            height=200,
            width=320)
        self.toplevel1.geometry("320x200")

        self.ip = tk.StringVar()
        self.port = tk.StringVar()

        self.con = Client()

        self.serv = Server()

        

        # toplevel1.maxsize(480, 640)
        # toplevel1.minsize(480, 640)
        self.ip_label = tk.Label(self.toplevel1)
        self.ip_label.configure(text='IP:')
        self.ip_label.place(anchor="nw", x=50, y=50)

        self.port_label = tk.Label(self.toplevel1)
        self.port_label.configure(text='Porta:')
        self.port_label.place(anchor="nw", x=50, y=75)

        self.port_entry = tk.Entry(self.toplevel1, textvariable=self.port)
        self.port_entry.place(anchor="nw", x=120, y=75)

        self.ip_entry = tk.Entry(self.toplevel1)
        self.ip_entry.place(anchor="nw", x=120, y=50)
        

        self.create_session_button = tk.Button(self.toplevel1, command=self.make_server_connection)
        # self.create_session_button.configure(text='Criar Sessao')
        self.create_session_button.configure(text='Servidor')
        self.create_session_button.place(anchor="nw", x=100, y=100)

        self.connect_button = tk.Button(self.toplevel1, command=self.make_client_connection)
        # self.connect_button.configure(text='Conectar')
        self.connect_button.configure(text='Cliente')
        self.connect_button.place(anchor="nw", x=200, y=100)

        self.ip_button = tk.Button(self.toplevel1, command=self.get_ip_function)
        self.ip_button.configure(text='Get Ip')
        self.ip_button.place(anchor="nw", x=150, y=150)

        
        self.test_button = tk.Button(self.toplevel1, command=self.create_new_window)
        self.test_button.configure(text='Chat')
        self.test_button.place(anchor="nw", x=250, y=150)
        
        self.title_label = tk.Label(self.toplevel1)
        self.title_label.configure(text='8B6T')
        self.title_label.place(anchor="n", x=160, y=10)

        self.toplevel1.pack_propagate(0)

        # Main widget
        if not self.con.client:
            self.mainwindow = self.toplevel1
            # self.mainwindow.destroy()
        else:
            self.mainwindow = self.msgWindow.mainwindow

        # Obj connection
        
    def run(self):
        self.mainwindow.mainloop()
        

    def get_ip_function(self):
        self.ip.set(self.con.get_ipv4())
        self.ip_entry.config(textvariable=self.ip,state="readonly")

        self.serv.host_ip = self.con.get_ipv4() 
        self.con.host_ip = self.con.get_ipv4()    
        self.serv.port = 3000
        self.con.port = 3000   

    def make_client_connection(self):
        self.con.host_ip = self.con.get_ipv4()                
        self.con.port = int(self.port.get())
        # self.con.client_connection()
        # self.con.create_connection()
        self.con.connect()

    def make_server_connection(self):
        self.serv.host_ip = self.con.get_ipv4()           
        self.serv.port = int(self.port.get())
        # if(self.serv.port != None):
        self.serv.create_server_connection()
        # self.serv.connect()
        # else:
        #     print('not ok')

    def create_new_window(self):
        if self.con.client or self.serv.server:
            print(self.serv.server)
            self.toplevel1.destroy()
            self.msgWindow = MessageWindow(self.con,self.serv)
            self.msgWindow.run()

    # def msg_window(self):
    #     self.msgWindow.run()





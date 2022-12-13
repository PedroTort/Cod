import tkinter as tk


class MessageWindow:
    def __init__(self, con, serv):
        # build ui
        toplevel2 = tk.Tk()
        toplevel2.configure(background="#ffaeff", height=200, width=200)
        toplevel2.geometry("800x600")
        self.text_output = tk.Text(toplevel2)
        self.text_output.configure(
            background="#e2e2e2",
            height=10,
            insertunfocussed="none",
            relief="flat",
            width=50)
        
        self.con = con
        self.serv = serv

        self.msg = tk.StringVar()

        self.text_output.place(anchor="nw", height=400, width=780, x=10, y=60)

        self.text_input = tk.Entry(toplevel2, textvariable=self.msg)
        self.text_input.place(anchor="nw", height=100, width=500, x=10, y=490)

        if self.serv.server:
            self.recive_button = tk.Button(toplevel2)
            self.recive_button.configure(text='Receber', command=self.recive_msg)
            self.recive_button.place(anchor="nw", x=700, y=520)

        elif self.con.client:
            self.send_button = tk.Button(toplevel2, command=self.send_msg)
            self.send_button.configure(text='Enviar')
            self.send_button.place(anchor="nw", x=700, y=520)

        self.reset_button = tk.Button(toplevel2)
        self.reset_button.configure(text='button2')
        self.reset_button.place(anchor="nw", x=700, y=470)

        self.title_label = tk.Label(toplevel2)
        self.title_label.configure(text=self.title())
        self.title_label.place(anchor="n", x=380, y=10)
        # Main widget
        self.mainwindow = toplevel2

        

    def run(self):
        self.mainwindow.mainloop()

    def title(self):
        if self.con.client:
            print('cliente')
            self.title_label.configure(text='Cliente')
        elif self.serv.server:
            print('servidor')
            self.title_label.configure(text='Servidor')

    def send_msg(self):
        # self.con.msg = self.msg.get()
        # print(self.con.msg)
        if self.con.client:
            self.con.send_msg(self.text_input.get())

    def recive_msg(self):
        if self.serv.server:
            msg = self.serv.recieve_message()
            print(msg)
            self.text_output.insert(tk.END, str(msg))
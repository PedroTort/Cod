import tkinter as tk


class MessageWindow:
    def __init__(self, master=None):
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
        self.text_output.place(anchor="nw", height=400, width=780, x=10, y=10)
        self.text_input = tk.Entry(toplevel2)
        self.text_input.place(anchor="nw", height=100, width=500, x=10, y=490)
        self.recive_button = tk.Button(toplevel2)
        self.recive_button.configure(text='button1')
        self.recive_button.place(anchor="nw", x=700, y=570)
        self.send_button = tk.Button(toplevel2)
        self.send_button.configure(text='button1')
        self.send_button.place(anchor="nw", x=700, y=520)
        self.reset_button = tk.Button(toplevel2)
        self.reset_button.configure(text='button1')
        self.reset_button.place(anchor="nw", x=700, y=470)

        # Main widget
        self.mainwindow = toplevel2

    def run(self):
        self.mainwindow.mainloop()

import string
import random
import tkinter as tk


class InputFrame(tk.Frame):
    def __init__(self, parent, *args, **krargs):
        tk.Frame.__init__(self, parent, *args, **krargs)
        self.parent = parent
        self.eText = tk.StringVar()
        self.char = string.ascii_letters+string.digits+'!@$%^&*()+*'
        self.btn = tk.Button(self.parent, text='lets start', command=lambda: self.password1(),
                             relief='raised', bg='lightgreen')
        self.btn.pack()
        self.txt1 = tk.Entry(self.parent, width=50, fg='black', bg='pink', font=(
            'calibri 10'), cursor='pencil', textvariable=self.eText)
        self.txt1.configure(state='readonly')
        self.txt1.pack()
        self.txt2 = tk.Entry(self.parent, width=20, fg='white', bg='black', font=('calibri 10'), cursor='pencil')
        self.txt2.bind('<Return>', lambda o: self.passcode())
        self.txt2.pack()
        self.txt3 = tk.Text(self.parent, width=50, fg='black', bg='skyblue', font=('calibri 10'), cursor='pencil')
        self.txt3.pack()

    def password1(self):
        print('here')
        self.eText.set("Please enter the length of your password:")

    def passcode(self):
        number = int(self.txt2.get())
        password = ''.join([random.choice(self.char) for i in range(number)])
        self.txt3.insert(tk.END, f'Your password is:{password}')


def run_gui():
    root = tk.Tk()
    root.title('Password')
    root.geometry('400x400')
    root.resizable(0, 0)
    frame = InputFrame(root)
    frame.pack()
    root.mainloop()


run_gui()

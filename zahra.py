import string
import random
from tkinter import *
root = Tk()
root.title('Password')
root.geometry('400x400')
root.resizable(0, 0)
char = string.ascii_letters+string.digits+'!@$%^&*()+*'


def password1():
    global eText
    eText.set("Please enter the length of your password:")


def passcode(event):
    global txt2
    number = int(txt2.get())
    password = ''.join([random.choice(char) for i in range(number)])
    txt3.insert(END, f'Your password is:{password}')


btn = Button(root, text='lets start', command=password1,
             relief='raised', bg='lightgreen').pack()

eText = StringVar()
txt1 = Entry(root, width=50, fg='black', bg='pink', font=(
    'calibri 10'), cursor='pencil', textvariable=eText)
txt1.configure(state='readonly')
txt1.pack()

txt2 = Entry(root, width=20, fg='white', bg='black',
             font=('calibri 10'), cursor='pencil')
txt2.bind('<Return>', passcode)

txt2.pack()
txt3 = Text(root, width=50, fg='black', bg='skyblue',
            font=('calibri 10'), cursor='pencil')
txt3.pack()

root.mainloop()

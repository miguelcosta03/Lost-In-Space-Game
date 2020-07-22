from tkinter import *

win = Tk()

img = PhotoImage(file="background.png")
Label(win, image=img, bg="grey").pack()
win.wm_attributes('-transparentcolor', 'grey')

# General GUI
password = Entry(win)
password.place(x=50, y=50)

b_encrypt = Button(win, text='ENCRYPT')
b_encrypt.place(x=200, y=50)

win.geometry('800x600')
win.mainloop()

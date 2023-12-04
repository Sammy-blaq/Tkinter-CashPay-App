from tkinter import *
from tkinter.ttk import *

# root screen
root = Tk()
root.geometry('200x600')

#mainframe
mainFrame = Frame(root, padding=15)
mainFrame.pack()

#phone Number label and Entry
phoneNoLbl = Label(root, text='Phone Number:')
phoneNoLbl.place(x=400, y=900)

phoneNoEntry = Entry(root)
phoneNumber = phoneNoEntry.get()
phoneNoEntry.place(x=400, y=960)

#Password label and Entry
passwordLbl = Label(root, text='Password:')
passwordLbl.place(x=400, y=1100)

passwordEntry = Entry(root)
password = passwordEntry.get()
passwordEntry.place(x=400, y=1160)

#Remember password checkbox
remember = Checkbutton(root, text='Remember Password')
remember.place(x=400, y=1250)

#Sign in Label and button
signInLbl = Label(root, text='Sign In')
signInLbl.place(x=25, y=20)

signInBtn = Button(root, text='Sign In')
signInBtn.place(x=400, y=1500)

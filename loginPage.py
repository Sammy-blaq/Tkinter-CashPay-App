from tkinter.ttk import *

# root screen
root = Tk()
root.geometry('400x800')

#mainframe
mainFrame = Frame(root, padding=15)
mainFrame.pack()

#phone Number label and Entry
phoneNoLbl = Label(root, text='Phone Number:')
phoneNoLbl.place(x=400, y=400)

phoneNoEntry = Entry(root)
phoneNumber = phoneNoEntry.get()
phoneNoEntry.place(x=400, y=460)

#Password label and Entry
passwordLbl = Label(root, text='Password:')
passwordLbl.place(x=400, y=560)

passwordEntry = Entry(root)
password = passwordEntry.get()
passwordEntry.place(x=400, y=620)

#Remember password checkbox
remember = Checkbutton(root, text='Remember Password')
remember.place(x=400, y=700)

#Sign in Label and button
signInLbl = Label(root, text='Sign In')
signInLbl.place(x=25, y=20)

signInBtn = Button(root, text='Sign In')
signInBtn.place(x=400, y=850)


createNewBtn = Button(root, text=' Create a New Account ')
createNewBtn.place(x=400, y=950)

root.mainloop()

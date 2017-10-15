from tkinter import *

class mainWindow():
    def create(self,root):
        root.title("welcome to quiz app!")
        root.geometry("500x500+200+10")

        main_label = Label(root, text='Welcome to Quiz App')
        logIn_button = Button(root, text='Log In', bd=5, command=loginPage)
        quit_button = Button(root, text='Quit', bd=5, command=quit)

        main_label.pack()
        logIn_button.pack()
        quit_button.pack()

def loginPage():
    root.destroy()
    import login

def quit():
    root.destroy()

root=Tk()
app=mainWindow()
app.create(root)
root.mainloop()




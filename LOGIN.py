from tkinter import *

root= Tk()
root.title("Log in")
root.geometry("500x500+200+10")
root.config(bg="black")
def loginPage():

    import LOGININPUT.py
    user=loggedInUser()
    display=user.currentUser()
    raise_frame(f2)
    Label(f2, text=display, fg="white", bg="black", font=font1).pack()
def finish():
        root.destroy()
def raise_frame(frame):
    frame.tkraise()

f1 = Frame(root, bg="white")
f2= Frame(root, bg="white")

for frame in (f1,f2):
   frame.grid(row=0, column=0, sticky='news')

font1="Century 16"
font2="Century 12"
Label(f1, text='Login or Signup', height=5, fg="white", bg="black", font=font1).pack()
Button(f1, text='Login', width=50, height=6, command=loginPage).pack(side=BOTTOM)
Button(f1, text='Signup',width=50, height=6, command=lambda:raise_frame(f2)).pack(side=BOTTOM)


raise_frame(f1)
root.mainloop()
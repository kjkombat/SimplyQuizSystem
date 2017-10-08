from tkinter import *
import tkinter.messagebox
import pymysql.connections


def finish():
    root.destroy()
def checkEntry():
    # Connect to the database
    connection = pymysql.connect(host='localhost',
                                 user='root',
                                 password='mysql',
                                 db='Quizzer',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)

    try:
        with connection.cursor() as cursor:
            # Create a new record
            sql = "SELECT userID FROM Instructor WHERE userName = %s AND password = %s"
            cursor.execute(sql, (userName.get(),password.get()))
            result = cursor.fetchone()#result stored of query
            if result is not None:#if password and userName match
                label3 = Label(root, text=result, height=5)
                label3.pack()
                class loggedInUser:
                    def __init__(self):
                        data=result

                    def currentUser(self):
                        return result

                finish()
            else: #if password and username do no match
                label3 = Label(root, text='Wrong userName/Password', height=5)
                label3.pack()



        # connection is not autocommit by default. So you must commit to save
        # your changes.
        #connection.commit()

        # with connection.cursor() as cursor:
        #     # Read a single record
        #     sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        #     cursor.execute(sql, ('webmaster@python.org',))
        #     result = cursor.fetchone()
        #     print(result)
    finally:
        connection.close()


root = Tk()
root.geometry=("500x500+200+10")


label1 = Label( root, text="Enter User Name",height=5,width=50)
userName = Entry(root, bd =5)

label2 = Label( root, text="Enter Password",height=5)
password = Entry(root, bd =5)

submit = Button(root, text ="Submit", command = checkEntry)


label1.pack()
userName.pack()
label2.pack()
password.pack()
submit.pack()
root.mainloop()





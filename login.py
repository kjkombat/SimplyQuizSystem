from tkinter import *
from userData import *
from student import *
import pymysql.connections
#creating connection to databse
connection = pymysql.connect(host='localhost',
                                     user='root',
                                     password='mysql',
                                     db='Quizzer',
                                     charset='utf8mb4',
                                     cursorclass=pymysql.cursors.DictCursor)

class logIn:
    def checkEntry(self):
        try:
            with connection.cursor() as cursor:
                # Create a new record
                sql = "SELECT userID FROM Instructor WHERE userName = %s AND password = %s"
                cursor.execute(sql, (userName.get(), password.get()))
                result = cursor.fetchone()  # result stored of query
                if result is not None:  # if password and userName match
                    label3 = Label(root, text="Success", height=5)
                    label3.pack()
                    save(1)
                    root.destroy()
                    import createQuiz
                else:# if password and username do no match
                    sql = "SELECT studentID FROM Student WHERE userName = %s AND password = %s"
                    cursor.execute(sql, (userName.get(), password.get()))
                    result = cursor.fetchone()
                    if result is not None:# result stored of query
                        label3 = Label(root, text="Success", height=5)
                        label3.pack()
                        root.destroy()
                        studentWindow(result)

                        save(1)

                    else:
                        label3 = Label(root, text='Wrong userName/Password', height=5)
                        label3.pack()
        finally:
            connection.close()

#main
root = Tk()
root.geometry=("500x500+200+10")

var=logIn()
label1 = Label( root, text="Enter User Name",height=5,width=50)
userName = Entry(root, bd =5)
label2 = Label( root, text="Enter Password",height=5)
password = Entry(root, bd =5)
submit = Button(root, text ="Submit", command =var.checkEntry)


label1.pack()
userName.pack()
label2.pack()
password.pack()
submit.pack()
root.mainloop()
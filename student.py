from tkinter import *
from database import *
from answerQuiz import*

class student:
    def checkQuizID(self,root,studentID,quizID):
        with connection.cursor() as cursor:
            sql = "SELECT `quizID`, `quizName`, `quizTime`, `maxScore` FROM `Quiz` WHERE `quizID` = %s"
            cursor.execute(sql,(quizID))
            result = cursor.fetchone()
            if result is not None:
                label3 = Label(root, text=result, height=5)
                label3.grid(row=3,column=2)
                createAnswerWindow(result)

            else:
                label3 = Label(root, text="wrong ID", height=5)
                label3.grid(row=3, column=2)




def studentWindow(result):
    std = student()
    root = Tk()
    root.geometry("500x500+200+10")
    quizLabel= Label(root,text="Enter the id of the Quiz you want to attempt")
    quizEntry= Entry(root, bd=5)
    quizBtn= Button(root,text="Go",command= lambda : std.checkQuizID(root,result['studentID'],quizEntry.get()) )

    quizLabel.grid(row=0,column=2)
    quizEntry.grid(row=1, column=1)
    quizBtn.grid(row=2, column=2)

from tkinter import *
from database import *
from createQuestions import *
from userData import *
class quiz:
    def enterValue(self):
        try:
            with connection.cursor() as cursor:
                sql="INSERT INTO `Quiz`(`quizName`, `quizTime`, `maxScore`) VALUES (%s,%s,%s)"
                cursor.execute(sql,(nameEntry.get(),timeEntry.get(),scoreEntry.get()))
            connection.commit()
            with connection.cursor() as cursor:
                sqlCheck="SELECT quizID FROM Quiz where quizName = %s"
                cursor.execute(sqlCheck,(nameEntry.get()))
                result= cursor.fetchone()
                if result is not None:
                    labelSuccess = Label(root, text="Success", height=5)
                    labelSuccess.grid(row=3,column=1)
                    submit.grid_forget()
                    self.createQuestionButtons(result)

                else:
                    labelFail = Label(root, text="Fail", height=5)
                    labelFail.grid(row=3, column=1)


        finally:
            var = 0
            #connection.close()
    def createMCQ(self,result):
        root2=Tk()
        MCQ(root2, result['quizID'])

    def createTrueFalse(self,result):
        root2=Tk()
        TrueFalse(root2, result['quizID'])

    def createQuestionButtons(self, result):
        MCQbtn = Button(root, text="MCQ", bd=5, command= lambda: self.createMCQ(result))
        trueFalse = Button(root,text="True/False",bd=5,command = lambda: self.createTrueFalse(result))
        MCQbtn.grid(row=6, column=0)
        trueFalse.grid(row=6,column=1)




root = Tk()
root.geometry=("500x500+200+10")
newQuiz=quiz()
nameLabel= Label(root,text="Enter Name of Quiz")
nameEntry= Entry(root,bd=5,)
timeLabel = Label(root, text="Enter time of Quiz")
timeEntry = Entry(root, bd=5, )
scoreLabel = Label(root, text="Enter score of Quiz")
scoreEntry = Entry(root, bd=5, )
submit=Button(root,text="Submit",bd=5,command=newQuiz.enterValue)

nameLabel.grid(row=0, column=0)
nameEntry.grid(row=0, column=1)
timeLabel.grid(row=1, column=0)
timeEntry.grid(row=1, column=1)
scoreLabel.grid(row=2, column=0)
scoreEntry.grid(row=2, column=1)
submit.grid(row=3, column=0)

root.mainloop()
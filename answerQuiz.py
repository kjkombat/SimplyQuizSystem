from database import *
from tkinter import *



def getMCQs(root,quiz):
    with connection.cursor() as cursor:
        sql = "SELECT * FROM `MCQs` WHERE `relatedToQuiz` = %s "
        cursor.execute(sql,(quiz))
        result= cursor.fetchall()
        print (result)
        global var
        var =  IntVar()
        radio = []
        data = []
        for row in result:
            questionLabel= Label(root,text=row['Question'] )
            data.append(0)
            radio.append(Radiobutton(root,text=row['op1'],variable= row['MCQID'],value=1))
            radio.append(Radiobutton(root,text=row['op2'],variable= row['MCQID'],value=2))
            radio.append(Radiobutton(root,text=row['op3'],variable= row['MCQID'],value=3))
            radio.append(Radiobutton(root,text=row['op4'],variable= row['MCQID'],value=4))
            radio.append(Button(root,text="Go!",command = lambda :checkMCQAnswer(row['MCQID'],row['MCQID'].get())))
            questionLabel.grid()
            for choices in radio:
                choices.grid()


def checkMCQAnswer(ID,ans):
    with connection.cursor() as cursor:
        print(ID,ans)
        sql = "SELECT `MCQID` FROM `MCQs` WHERE `correct`= %s AND `MCQID` = %s "
        cursor.execute(sql,(ans,ID))
        result = cursor.fetchone()
        if result is not None:
           print ("correct")

        else:
            print("wrong")








def createAnswerWindow(result):
    global total
    global correct
    total = 0
    correct = 0

    root = Tk()
    root.title(result['quizName'])
    getMCQs(root,result['quizID'])














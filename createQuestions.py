from tkinter import *
from database import *
class questions:
    def MCQEntry(self,root,ID,questionEntry,correctEntry,opt1Entry,opt2Entry,opt3Entry,opt4Entry):
        with connection.cursor() as cursor:
            sql = "INSERT INTO `MCQs`(`relatedToQuiz`, `Question`, `op1`, `op2`, `op3`, `op4`, `correct`) VALUES (%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, (ID, questionEntry.get(), opt1Entry.get(), opt2Entry.get(), opt3Entry.get(), opt4Entry.get(),
            correctEntry.get()))
            connection.commit()
            root.destroy()
            newRoot=Tk()
            MCQ(newRoot,ID)

    def TFEntry(self,root,ID,questionEntry,correctEntry,trueEntry,falseEntry):
            with connection.cursor() as cursor:
                sql = "INSERT INTO `trueFalse`(`relatedToQuiz`, `TFquestion`, `trueOP`, `falseOP`, `correctOP`) VALUES (%s,%s,%s,%s,%s)"
                cursor.execute(sql,(ID,questionEntry.get(),trueEntry.get(),falseEntry.get(),correctEntry.get()))
                connection.commit()
                root.destroy()
                newRoot=Tk()
                TrueFalse(newRoot,ID)







def MCQ(root,ID):
    mcq1=questions()
    questionLabel = Label(root, text="Enter Question")
    questionEntry = Entry(root, bd=5)
    optionLabel = Label(root, text="Enter 4 options for MCQ")
    correctLabel = Label(root, text="Enter in number(1-4) the correct option")
    opt1Entry = Entry(root, bd=5)
    opt2Entry = Entry(root, bd=5)
    opt3Entry = Entry(root, bd=5)
    opt4Entry = Entry(root, bd=5)
    correctEntry = Entry(root, bd=5)
    add = Button(root, text="Add", bd=5, command= lambda : mcq1.MCQEntry(root,ID,questionEntry,correctEntry,opt1Entry,opt2Entry,opt3Entry,opt4Entry))
    finish = Button(root, text="Finish", command= lambda : root.destroy())
    #add = Button(root, text="Add", bd=5)

    questionLabel.grid(row=0, column=0)
    questionEntry.grid(row=0, column=1)
    correctLabel.grid(row=0, column=2)
    correctEntry.grid(row=0, column=3)
    optionLabel.grid(row=1, column=0)
    opt1Entry.grid(row=2, column=1)
    opt2Entry.grid(row=3, column=1)
    opt3Entry.grid(row=4, column=1)
    opt4Entry.grid(row=5, column=1)
    add.grid(row=6, column=1)
    finish.grid(row=6, column=0)

def TrueFalse(root, ID):

    TF1=questions()
    questionLabel = Label(root, text="Enter Question")
    questionEntry = Entry(root, bd=5)
    trueLabel = Label(root, text="Enter True Option")
    trueEntry = Entry(root, bd=5)
    falseOption = Label(root, text="Enter False Option")
    falseEntry = Entry(root, bd=5)
    correctLabel = Label(root, text="Enter (T/F) for the correct option")
    correctEntry = Entry(root, bd=5)
    add = Button(root, text="Add", bd=5, command= lambda : TF1.TFEntry(root,ID,questionEntry,correctEntry,trueEntry,falseEntry))
    finish = Button(root, text="Finish", command= lambda : root.destroy())


    questionLabel.grid(row=0, column=0)
    questionEntry.grid(row=0, column=1)
    correctLabel.grid(row=0, column=2)
    correctEntry.grid(row=0, column=3)
    trueLabel.grid(row=1,column=0)
    trueEntry.grid(row=1, column=1)
    falseOption.grid(row=2, column=0)
    falseEntry.grid(row=2, column=1)
    add.grid(row=3, column=0)
    finish.grid(row=3, column=1)















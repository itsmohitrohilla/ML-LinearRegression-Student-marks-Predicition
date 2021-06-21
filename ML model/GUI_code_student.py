from tkinter import *
import joblib

clf = joblib.load("student_marks_preduction_ml_model.pkl")

tr = Tk()


def model(self):
    ex = textfield_data.get()
    ex1 = float(ex)
    answer = clf.predict([[ex1]])[0][0].round(5)

    #return answer
    ans = Label(tr, text= answer, bg = 'yellow', font="lucida 35 bold")
    ans.pack(side=BOTTOM,pady = 6)
    ans.place(relx = 0.5, rely = 0.7, anchor = 'center')
    name3 = Label(tr, text="Student will get approx these marks \n if He/she study as much given hours in a day", font="Verdana 15 bold")
    name3.pack(side= BOTTOM,pady = 6)
    name3.place(relx = 0.5, rely = 0.6, anchor = 'center')

    #textfield_data.insert(0,answer)
    

tr.title("ML Linear Regression Algorithm")
tr.geometry("580x430")

#Label name
name = Label(tr, text="STUDENT MARKS PREDICTION",bg = 'yellow', font="lucida 35 bold")
name.pack(side=TOP,pady = 6)
name2 = Label(tr, text="- Enter Student Study Hours - ", font="Verdana 15 bold")
name2.pack(side=TOP,pady = 6)

#text enter
textfield_data = Entry(tr , font = "lucida 50 bold",width = 10, relief='solid',justify = RIGHT)
textfield_data.pack(side = TOP,pady = 2,padx=8)

#button
submit_frame = Frame(tr)
submit_frame.pack(side=TOP)
submit = Button(submit_frame, text="Submit",font="lucida 25 bold",width = 10, relief='solid', command = model)
submit.grid(row=3,column=0,padx=5 , pady=5)

submit.bind('<Button-1>',model)

tr.mainloop()

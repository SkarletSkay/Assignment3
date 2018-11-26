from tkinter import *
import Tables

conn = Tables.create_connection()


def Quit():
    global root
    root.destroy()


def raise_frame(frame):
    frame.tkraise()


def query1():
    c = conn.cursor()
    c.execute('SELECT car_id, colour, plate_number FROM Cars AS C WHERE C.colour="red" AND C.plate_number LIKE "AN%"')
    all_rows = c.fetchall()
    answer = 'car_id\tcolour\tplate_number\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t'
        answer += "\n"
    answer1['text'] = answer


def query2(input):
    answer2['text'] = input


def query3():
    answer3['text'] = 'to be done'


def query4():
    answer4['text'] = 'to be done'


def query5():
    answer5['text'] = 'to be done'


def query6():
    answer6['text'] = 'to be done'


def query7():
    answer7['text'] = 'to be done'


def query8():
    answer8['text'] = 'to be done'


def query9():
    answer9['text'] = 'to be done'


def query10():
    answer10['text'] = 'to be done'


root = Tk()
initial = Frame(root)
q1 = Frame(root)
q2 = Frame(root)
q3 = Frame(root)
q4 = Frame(root)
q5 = Frame(root)
q6 = Frame(root)
q7 = Frame(root)
q8 = Frame(root)
q9 = Frame(root)
q10 = Frame(root)

for frame in (initial, q1, q2, q3, q4, q5, q6, q7, q8, q9, q10):
    frame.grid(row=0, column=0, sticky='news')
# init frame
Label(initial, text='Welcome to our little database!').pack()
Button(initial, text='Go to query 1', command=lambda: raise_frame(q1)).pack()
Button(initial, text='Go to query 2', command=lambda: raise_frame(q2)).pack()
Button(initial, text='Go to query 3', command=lambda: raise_frame(q3)).pack()
Button(initial, text='Go to query 4', command=lambda: raise_frame(q4)).pack()
Button(initial, text='Go to query 5', command=lambda: raise_frame(q5)).pack()
Button(initial, text='Go to query 6', command=lambda: raise_frame(q6)).pack()
Button(initial, text='Go to query 7', command=lambda: raise_frame(q7)).pack()
Button(initial, text='Go to query 8', command=lambda: raise_frame(q8)).pack()
Button(initial, text='Go to query 9', command=lambda: raise_frame(q9)).pack()
Button(initial, text='Go to query 10', command=lambda: raise_frame(q10)).pack()
Button(initial, text='Exit', command=lambda: Quit()).pack()

# q1 frame no input
Label(q1, text='A customer claims she forgot her bag in a car and asks to help.\nShe was using cars several times this day, but she believes the right car was red and its plate starts with “AN”. ').pack()
Button(q1, text='Run query', command=lambda: query1()).pack()
Button(q1, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer1 = Label(q1, text="  ")
answer1.pack()

# q2 frame input: date
Label(q2, text='This is the result of querry 2!\nPlease enter input date').pack()
input2 = Entry(q2)
input2.pack()
Button(q2, text='Run query', command=lambda: query2(input2.get())).pack()
Button(q2, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer2 = Label(q2, text="")
answer2.pack()

# q3 frame no input
Label(q3, text='This is the result of querry 3!').pack()
Button(q3, text='Run query', command=lambda: query3()).pack()
Button(q3, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer3 = Label(q3, text="")
answer3.pack()

# q4 frame
Label(q4, text='This is the result of querry 4!').pack()
Button(q4, text='Run query', command=lambda: query4()).pack()
Button(q4, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer4 = Label(q4, text="")
answer4.pack()

# q5 frame
Label(q5, text='This is the result of querry 5!').pack()
Button(q5, text='Run query', command=lambda: query5()).pack()
Button(q5, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer5 = Label(q5, text="")
answer5.pack()

# q6 frame
Label(q6, text='This is the result of querry 6!').pack()
Button(q6, text='Run query', command=lambda: query6()).pack()
Button(q6, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer6 = Label(q6, text="")
answer6.pack()

# q7 frame
Label(q7, text='This is the result of querry 7!').pack()
Button(q7, text='Run query', command=lambda: query7()).pack()
Button(q7, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer7 = Label(q7, text="")
answer7.pack()

# q8 frame
Label(q8, text='This is the result of querry 8!').pack()
Button(q8, text='Run query', command=lambda: query8()).pack()
Button(q8, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer8 = Label(q8, text="")
answer8.pack()

# q9 frame
Label(q9, text='This is the result of querry 9!').pack()
Button(q9, text='Run query', command=lambda: query9()).pack()
Button(q9, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer9 = Label(q9, text="")
answer9.pack()

# q10 frame
Label(q10, text='This is the result of querry 10!').pack()
Button(q10, text='Run query', command=lambda: query10()).pack()
Button(q10, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer10 = Label(q10, text="")
answer10.pack()

raise_frame(initial)
root.mainloop()
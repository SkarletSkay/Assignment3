from tkinter import *
import Tables
import sqlite3 as sql

conn = Tables.create_connection()


def Quit():
    global root
    root.destroy()


def raise_frame(frame):
    frame.tkraise()


def query1():
    answer1 = []
    c = conn.cursor()
    c.execute('SELECT DISTINCT C.car_id, C.colour, C.plate_number FROM Orders AS O, Cars AS C  WHERE C.colour="Red" AND C.plate_number LIKE "AN%" AND O.car_id = C.car_id ')
    all_rows = c.fetchall()
    answer1.append(Label(q1, text=" ").grid(row=2, column=0, columnspan=5))
    answer1.append(Label(q1, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan =5, sticky="w e"))
    answer1.append(Label(q1, text=" ", bg="gray90").grid(row=4, column=0, columnspan=5, sticky="w e"))
    answer1.append(Label(q1, text="Car ID",bg="gray90").grid(row=4,column=0, sticky="w e"))
    answer1.append(Label(q1, text="Colour",bg="gray90").grid(row=4, column=2, sticky="w e"))
    answer1.append(Label(q1, text="Plate Number",bg="gray90").grid(row=4, column=4, sticky="w e"))
    for i in range(len(all_rows)):
        answer1.append(Label(q1, text=all_rows[i][0]).grid(row = 5+i,column=0))
        answer1.append(Label(q1, text=all_rows[i][1]).grid(row = 5+i,column=2))
        answer1.append(Label(q1, text=all_rows[i][2]).grid(row = 5+i,column=4))




def query2(input):
    answer2 = []
    c = conn.cursor()
    c.execute(
        'SELECT CAST ((start_time-julianday("00:00:00"))*24 AS INT), count(*) FROM Charges AS C WHERE date = julianday("' + input + '") GROUP BY CAST ((start_time-julianday("00:00:00"))*24 AS INT)')
    all_rows = c.fetchall()
    answer2.append(Label(q2, text=" ").grid(row=3, column=0, columnspan=2))
    answer2.append(Label(q2, text="Table of results", bg="gray80").grid(row=4, column=0, columnspan=2, sticky="w e"))
    answer2.append(Label(q2, text=" ", bg="gray90").grid(row=5, column=0, columnspan=2, sticky="w e"))
    answer2.append(Label(q2, text="Hours", bg="gray90").grid(row=5, column=0, sticky="w e"))
    answer2.append(Label(q2, text="Plugs Accupied", bg="gray90").grid(row=5, column=1, sticky="w e"))
    for i in range(len(all_rows)):
        # answer2.append(Label(q2, text=str(all_rows[i][0])+"-"+str(all_rows[i][0]+1)).grid(row=6 + i, column=0))
        answer2.append(Label(q2, text=all_rows[i][0]).grid(row=6 + i, column=0))
        answer2.append(Label(q2, text=all_rows[i][1]).grid(row=6 + i, column=1))

    answer2 = []




def query3():
    answer3 = []
    answer3.append(Label(q3, text=" ").grid(row=2, column=0, columnspan=5))
    answer3.append(Label(q3, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=5, sticky="w e"))
    answer3.append(Label(q3, text=" ", bg="gray90").grid(row=4, column=0, columnspan=5, sticky="w e"))
    answer3.append(Label(q3, text="Morning", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer3.append(Label(q3, text="Afternoon", bg="gray90").grid(row=4, column=2, sticky="w e"))
    answer3.append(Label(q3, text="Evening", bg="gray90").grid(row=4, column=4, sticky="w e"))

    c = conn.cursor()
    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2) FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("06:59:59") AND O.start_time<julianday("10:00:00")')
    all_rows = c.fetchall()
    answer3.append(Label(q3, text=all_rows[0][0]).grid(row=5, column=0))

    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2)FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("11:59:59") AND O.start_time<julianday("14:00:00")')
    all_rows = c.fetchall()
    answer3.append(Label(q3, text=all_rows[0][0]).grid(row=5, column=2))

    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2) FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("16:59:59") AND O.start_time<julianday("19:00:00")')
    all_rows = c.fetchall()
    answer3.append(Label(q3, text=all_rows[0][0]).grid(row=5, column=4))



def query4():
    answer4 = []
    answer4.append(Label(q4, text=" ").grid(row=2, column=0, columnspan=5))
    answer4.append(Label(q4, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=5, sticky="w e"))
    answer4.append(Label(q4, text=" ", bg="gray90").grid(row=4, column=0, columnspan=5, sticky="w e"))
    answer4.append(Label(q4, text="Customer ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer4.append(Label(q4, text="Full name", bg="gray90").grid(row=4, column=2, sticky="w e"))
    answer4.append(Label(q4, text="Order ID", bg="gray90").grid(row=4, column=4, sticky="w e"))

    c = conn.cursor()
    c.execute(
        'SELECT T.customer_id, C.full_name, T.order_id FROM (SELECT order_id, customer_id, COUNT(*) AS amount FROM Payments GROUP BY customer_id, order_id) AS T, Customers AS C WHERE T.amount>1 AND C.customer_id = T.customer_id')
    all_rows = c.fetchall()
    print(all_rows)
    if len(all_rows) == 0:
        answer4.append(Label(q4, text="No duplicated payments were indicated!").grid(row=5, column=0, columnspan=5, sticky="w e"))
    else:
        for i in range(len(all_rows)):
            answer4.append(Label(q4, text=all_rows[i][0]).grid(row = 5+i,column=0))
            answer4.append(Label(q4, text=all_rows[i][1]).grid(row = 5+i,column=2))
            answer4.append(Label(q4, text=all_rows[i][2]).grid(row = 5+i,column=4))


def query5(input):
    answer5 = []
    answer5.append(Label(q5, text=" ").grid(row=2, column=0, columnspan=5))
    answer5.append(Label(q5, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=5, sticky="w e"))
    answer5.append(Label(q5, text=" ", bg="gray90").grid(row=4, column=0, columnspan=5, sticky="w e"))
    answer5.append(Label(q5, text="Car ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer5.append(Label(q5, text="Average Distance (km)", bg="gray90").grid(row=4, column=2, sticky="w e"))
    answer5.append(Label(q5, text="Average time (sec)", bg="gray90").grid(row=4, column=4, sticky="w e"))
    c = conn.cursor()
    c.execute(
        'SELECT car_id,AVG(distance), AVG((end_time-start_time)*86400) FROM Orders AS O WHERE O.date = julianday("' + input + '") GROUP BY car_id')
    all_rows = c.fetchall()
    for i in range(len(all_rows)):
        answer5.append(Label(q5, text=all_rows[i][0]).grid(row = 5+i,column=0))
        answer5.append(Label(q5, text=round(all_rows[i][1])).grid(row = 5+i,column=2))
        answer5.append(Label(q5, text=round(all_rows[i][2])).grid(row = 5+i,column=4))



def query6():
    answer6 = []
    answer6.append(Label(q6, text=" ").grid(row=2, column=0, columnspan=2))

    c = conn.cursor()
    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("06:59:59") AND O.start_time<julianday("10:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer6.append(Label(q6, text="Top 3 pick up locations in the Morning (7AM-10AM):", bg="gray80").grid(row=3, column=0, columnspan=2, sticky="w e"))
    answer6.append(Label(q6, text=" ", bg="gray90").grid(row=4, column=0, columnspan=2, sticky="w e"))
    answer6.append(Label(q6, text="Location", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer6.append(Label(q6, text="Number of orders", bg="gray90").grid(row=4, column=1, sticky="w e"))
    h1 = len(all_rows)
    if len(all_rows) == 0:
        answer6.append(Label(q6, text="-").grid(row=5 , column=0))
        answer6.append(Label(q6, text="-").grid(row=5 , column=1))
        h1=1
    else:
        for i in range(h1):
            answer6.append(Label(q6, text=all_rows[i][0]).grid(row=5 + i, column=0))
            answer6.append(Label(q6, text=all_rows[i][1]).grid(row=5 + i, column=1))

    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("11:59:59") AND O.start_time<julianday("14:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer6.append(Label(q6, text="Top 3 pick up locations in the Afternoon (12PM-2PM):", bg="gray80").grid(row=6+h1, column=0,columnspan=2,sticky="w e"))
    answer6.append(Label(q6, text=" ", bg="gray90").grid(row=7+h1, column=0, columnspan=2, sticky="w e"))
    answer6.append(Label(q6, text="Location", bg="gray90").grid(row=7+h1, column=0, sticky="w e"))
    answer6.append(Label(q6, text="Number of orders", bg="gray90").grid(row=7+h1, column=1, sticky="w e"))
    h2 = len(all_rows)
    if len(all_rows) == 0:
        answer6.append(Label(q6, text="-").grid(row=8 +h1, column=0))
        answer6.append(Label(q6, text="-").grid(row=8 +h1 , column=1))
        h2=1
    else:
        for i in range(h2):
            answer6.append(Label(q6, text=all_rows[i][0]).grid(row=8+h1 + i, column=0))
            answer6.append(Label(q6, text=all_rows[i][1]).grid(row=8+h1 + i, column=1))

    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("16:59:59") AND O.start_time<julianday("19:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer6.append(
        Label(q6, text="Top 3 pick up locations in the Evening (5PM-7PM):", bg="gray80").grid(row=8 + h1+h2, column=0,
                                                                                                 columnspan=2,
                                                                                                 sticky="w e"))
    answer6.append(Label(q6, text=" ", bg="gray90").grid(row=9 + h1 +h2, column=0, columnspan=2, sticky="w e"))
    answer6.append(Label(q6, text="Location", bg="gray90").grid(row=9 + h1+h2, column=0, sticky="w e"))
    answer6.append(Label(q6, text="Number of orders", bg="gray90").grid(row=9 + h1+h2, column=1, sticky="w e"))
    if len(all_rows) == 0:
        answer6.append(Label(q6, text="-").grid(row=10 +h1+h2, column=0))
        answer6.append(Label(q6, text="-").grid(row=10 +h1+h2 , column=1))
    else:
        for i in range(len(all_rows)):
            answer6.append(Label(q6, text=all_rows[i][0]).grid(row=10 + h1+h2 + i, column=0))
            answer6.append(Label(q6, text=all_rows[i][1]).grid(row=10 + h1+h2 + i, column=1))


def query7():
    answer7 = []
    answer7.append(Label(q7, text=" ").grid(row=2, column=0, columnspan=2))
    answer7.append(Label(q7, text="Table of results", bg="gray80").grid(row=3, column=0,columnspan=2,sticky="w e"))
    answer7.append(Label(q7, text=" ", bg="gray90").grid(row=4, column=0, columnspan=2, sticky="w e"))
    answer7.append(Label(q7, text="Car ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer7.append(Label(q7, text="Number of orders", bg="gray90").grid(row=4, column=1, sticky="w e"))
    c = conn.cursor()
    c.execute(
        'SELECT car_id, COUNT(car_id)FROM Orders GROUP BY car_id ORDER BY COUNT(car_id) LIMIT round((SELECT COUNT(*) FROM Cars)/10)')
    all_rows = c.fetchall()
    for i in range(len(all_rows)):
        answer7.append(Label(q7, text=all_rows[i][0]).grid(row=5 + i, column=0))
        answer7.append(Label(q7, text=all_rows[i][1]).grid(row=5 + i, column=1))


def query8():
    answer8 = []
    answer8.append(Label(q8, text=" ").grid(row=2, column=0, columnspan=2))
    answer8.append(Label(q8, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=2, sticky="w e"))
    answer8.append(Label(q8, text=" ", bg="gray90").grid(row=4, column=0, columnspan=2, sticky="w e"))
    answer8.append(Label(q8, text="Customer ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer8.append(Label(q8, text="Number of Charges", bg="gray90").grid(row=4, column=1, sticky="w e"))
    c = conn.cursor()
    c.execute('SELECT customer_id, COUNT(customer_id) FROM Orders AS O, Charges AS CH  WHERE O.date = CH.date AND O.car_id = CH.car_id AND (julianday("now") - O.date)<31 GROUP by customer_id')
    all_rows = c.fetchall()
    for i in range(len(all_rows)):
        answer8.append(Label(q8, text=all_rows[i][0]).grid(row=5 + i, column=0))
        answer8.append(Label(q8, text=all_rows[i][1]).grid(row=5 + i, column=1))


def query9():
    answer9 = []
    answer9.append(Label(q9, text=" ").grid(row=2, column=0, columnspan=5))
    answer9.append(Label(q9, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=5, sticky="w e"))
    answer9.append(Label(q9, text=" ", bg="gray90").grid(row=4, column=0, columnspan=5, sticky="w e"))
    answer9.append(Label(q9, text="Workshop ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer9.append(Label(q9, text="Part Type ID", bg="gray90").grid(row=4, column=2, sticky="w e"))
    answer9.append(Label(q9, text="Amount pet week", bg="gray90").grid(row=4, column=4, sticky="w e"))
    c = conn.cursor()
    c.execute(
        'SELECT wid,  part_type_id, MAX(avg_use) FROM '
        '(SELECT wid, part_type_id, AVG(use) AS avg_use FROM'
        '(SELECT CAST(R.date/7 AS INT) AS week, wid, part_type_id, COUNT(*) AS use FROM Repairs AS R GROUP BY wid, part_type_id, CAST(R.date/7 AS INT)) '
        'GROUP BY wid, part_type_id)'
        'GROUP BY wid HAVING MAX(avg_use)')
    all_rows = c.fetchall()
    for i in range(len(all_rows)):
        answer9.append(Label(q9, text=all_rows[i][0]).grid(row = 5+i,column=0))
        answer9.append(Label(q9, text=round(all_rows[i][1])).grid(row = 5+i,column=2))
        answer9.append(Label(q9, text=round(all_rows[i][2])).grid(row = 5+i,column=4))


def query10():
    answer10 = []
    answer10.append(Label(q10, text=" ").grid(row=2, column=0, columnspan=2))
    answer10.append(Label(q10, text="Table of results", bg="gray80").grid(row=3, column=0, columnspan=2, sticky="w e"))
    answer10.append(Label(q10, text=" ", bg="gray90").grid(row=4, column=0, columnspan=2, sticky="w e"))
    answer10.append(Label(q10, text="Car Type ID", bg="gray90").grid(row=4, column=0, sticky="w e"))
    answer10.append(Label(q10, text="Total cost", bg="gray90").grid(row=4, column=1, sticky="w e"))
    c = conn.cursor()
    c.execute(
        'SELECT C.car_type_id, AVG(R.AvgRcost + Ch.AvgCHcost) FROM Cars AS C, '
        '(SELECT car_id, AVG(Rcost) AS AvgRcost FROM (SELECT car_id, SUM(cost) AS Rcost, Re.date FROM Repairs AS Re GROUP BY car_id, Re.date ) GROUP BY car_id) AS R, '
        '(SELECT car_id, AVG(CHcost) AS AvgCHcost FROM (SELECT  car_id, SUM(cost) AS CHcost, CHa.date FROM Charges AS CHa GROUP BY car_id, Cha.date) GROUP BY car_id) AS CH '
        ' WHERE C.car_id = R.car_id AND C.car_id = CH.car_id GROUP BY C.car_type_id ORDER BY AVG(R.AvgRcost + Ch.AvgCHcost) DESC LIMIT 1')
    all_rows = c.fetchall()
    for i in range(len(all_rows)):
        answer10.append(Label(q10, text=all_rows[i][0]).grid(row=5 + i, column=0))
        answer10.append(Label(q10, text=all_rows[i][1]).grid(row=5 + i, column=1))


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
Label(q1,
      text='A customer claims she forgot her\n bag in a car and asks to help.\n'
           'She was using cars several times this day,\n but she believes the right car was red and its plate starts with “AN”. ').grid(column=0, row=0, columnspan =5)
Button(q1, text='Run query', command=lambda: query1()).grid(row = 1, column = 1)
Button(q1, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 3)
answer1 = []
for x in range(5):
  Grid.columnconfigure(q1, x, weight=1)


answer2 = []


# q2 frame input: date
Label(q2, text='Compute how many sockets were occupied each hour.').grid(column=0, row=0, columnspan =2)
Label(q2, text='Date as YYYY-MM-DD:').grid(column=0, row=1)
input2 = Entry(q2)
input2.grid(row = 1, column = 1)
Button(q2, text='Run query', command=lambda: query2(input2.get())).grid(row = 2, column = 0)
Button(q2, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 2, column = 1)
for x in range(2):
  Grid.columnconfigure(q2, x, weight=1)

answer2 = []

# q3 frame no input
Label(q3, text='Gather statistics for one week on \n how many cars are busy (% to the total amount of taxis)').grid(column=0, row=0, columnspan =5)
Button(q3, text='Run query', command=lambda: query3()).grid(row = 1, column = 1)
Button(q3, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 3)
answer3 = []
for x in range(5):
  Grid.columnconfigure(q3, x, weight=1)

answer2 = []


# q4 frame
Label(q4, text='Find duplicating payments\n').grid(column=0, row=0, columnspan =5)
Label(q4, text='        ').grid(row = 1, column = 0)
Button(q4, text='Run query', command=lambda: query4()).grid(row = 1, column = 1)
Label(q4, text='        ').grid(row = 1, column = 2)
Button(q4, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 3)
answer4 = []
for x in range(5):
  Grid.columnconfigure(q4, x, weight=1)


answer2 = []

# q5 frame
input5= Entry(q5)
input5.grid(column=3, row=0, columnspan =2, sticky="")
Label(q5, text='Enter date in form YYYY-MM-DD \nto get statistics on  Average distance   \n and Average trip duration \n').grid(column=0, row=0, columnspan =3)
Label(q5, text='        ').grid(row = 1, column = 0)
Button(q5, text='Run query', command=lambda: query5(input5.get())).grid(row = 1, column = 1)
Label(q5, text='        ').grid(row = 1, column = 2)
Button(q5, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 3)
for x in range(5):
  Grid.columnconfigure(q5, x, weight=1)


# q6 frame
Label(q6, text='Compute top-3 most popular pick-up locations\n').grid(column=0, row=0, columnspan =2)
Button(q6, text='Run query', command=lambda: query6()).grid(row = 1, column = 0)
Button(q6, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 1)
answer6 = []
for x in range(2):
  Grid.columnconfigure(q6, x, weight=1)

# q7 frame
Label(q7, text='Find 10% of cars which take least amount of orders\n for the last 3 months\n').grid(column=0, row=0, columnspan =2)
Button(q7, text='Run query', command=lambda: query7()).grid(row = 1, column = 0)
Button(q7, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 1)
answer7 = []
for x in range(2):
  Grid.columnconfigure(q7, x, weight=1)

# q8 frame
Label(q8, text='Statistics for one month on how full sum of car charges at day of order\n depends on customer`s location').grid(column=0, row=0, columnspan =2)
Button(q8, text='Run query', command=lambda: query8()).grid(row = 1, column = 0)
Button(q8, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 1)
answer8 = []
for x in range(2):
  Grid.columnconfigure(q8, x, weight=1)

# q9 frame
Label(q9, text='Find parts which are used the most\n every week by every workshop\n').grid(column=0, row=0, columnspan =5)
Label(q9, text='        ').grid(row = 1, column = 0)
Button(q9, text='Run query', command=lambda: query9()).grid(row = 1, column = 1)
Label(q9, text='        ').grid(row = 1, column = 2)
Button(q9, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 3)
answer9 = []
for x in range(5):
  Grid.columnconfigure(q9, x, weight=1)

# q10 frame
Label(q10, text='Find car type which had the highest average cost (per day) of\n repairs and charging (combined)\n').grid(column=0, row=0, columnspan =2)
Button(q10, text='Run query', command=lambda: query10()).grid(row = 1, column = 0)
Button(q10, text='Back to menu', command=lambda: raise_frame(initial)).grid(row = 1, column = 1)
answer10 = []
for x in range(2):
  Grid.columnconfigure(q10, x, weight=1)

raise_frame(initial)
root.mainloop()

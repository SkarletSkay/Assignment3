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
    c = conn.cursor()
    c.execute('SELECT DISTINCT C.car_id, C.colour, C.plate_number FROM Orders AS O, Cars AS C  WHERE C.colour="Red" AND C.plate_number LIKE "AN%" AND O.car_id = C.car_id ')
    all_rows = c.fetchall()
    answer = 'car_id\tcolour\tplate_number\torder_id\tname\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t'
        answer += "\n"
    answer1['text'] = answer


def query2(input):
    c = conn.cursor()
    c.execute(
        'SELECT CAST ((start_time-julianday("00:00:00"))*24 AS INT), count(*) FROM Charges AS C WHERE date = julianday("' + input + '") GROUP BY CAST ((start_time-julianday("00:00:00"))*24 AS INT)')
    all_rows = c.fetchall()
    answer = 'Hours\tPlugs Accupied\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t'
        answer += "\n"
    answer2['text'] = answer


def query3():
    c = conn.cursor()
    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2) FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("06:59:59") AND O.start_time<julianday("10:00:00")')
    all_rows = c.fetchall()
    answer = 'Morning\t\tAfternoon\t\tEvening\n'+str(all_rows[0][0])+'\t\t\t'
    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2)FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("11:59:59") AND O.start_time<julianday("14:00:00")')
    all_rows = c.fetchall()
    answer += str(all_rows[0][0]) + '\t\t\t'
    c.execute(
        'SELECT round((COUNT( DISTINCT car_id)*1.0)/(SELECT COUNT(*) FROM Cars)*100,2) FROM Orders AS O WHERE (julianday("now") - O.date)<7.0 AND O.start_time>julianday("16:59:59") AND O.start_time<julianday("19:00:00")')
    all_rows = c.fetchall()
    answer += str(all_rows[0][0])
    answer3['text'] = answer


def query4():
    c = conn.cursor()
    c.execute(
        'SELECT T.customer_id, C.full_name, T.order_id FROM (SELECT order_id, customer_id, COUNT(*) AS amount FROM Payments GROUP BY customer_id, order_id) AS T, Customers AS C WHERE T.amount>1 AND C.customer_id = T.customer_id')
    all_rows = c.fetchall()
    answer = 'Customer ID\tFull name\tOrder ID\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t'
        answer += "\n"
    answer4['text'] = answer


def query5(input):
    c = conn.cursor()
    c.execute(
        'SELECT car_id,AVG(distance), AVG((end_time-start_time)*86400) FROM Orders AS O WHERE O.date = julianday("' + input + '") GROUP BY car_id')
    all_rows = c.fetchall()
    answer = 'Car ID\t\tAverage Distance\t\tAverage time\n\t\t'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n\t\t"
    answer5['text'] = answer


def query6():
    c = conn.cursor()
    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("06:59:59") AND O.start_time<julianday("10:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer = 'Top 3 pick up locations in the Morning (7AM-10AM):\nLocation\t\tNumber of orders\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"

    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("11:59:59") AND O.start_time<julianday("14:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer += '\nTop 3 pick up locations in the Afternoon (12PM-2PM):\nLocation\t\tNumber of orders\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"

    c.execute(
        'SELECT init_location, COUNT(init_location) FROM Orders AS O WHERE O.start_time>julianday("16:59:59") AND O.start_time<julianday("19:00:00") GROUP BY init_location ORDER BY COUNT(init_location) DESC LIMIT 3 ')
    all_rows = c.fetchall()
    answer += '\nTop 3 pick up locations in the Evening (5PM-7PM):\nLocation\t\tNumber of orders\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"
    answer6['text'] = answer


def query7():
    c = conn.cursor()
    c.execute(
        'SELECT car_id, COUNT(car_id)FROM Orders GROUP BY car_id ORDER BY COUNT(car_id) LIMIT round((SELECT COUNT(*) FROM Cars)/10)')
    all_rows = c.fetchall()
    answer = 'Car ID\t\tNumber of orders\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"
    answer7['text'] = answer


def query8():
    c = conn.cursor()
    c.execute('SELECT customer_id, COUNT(customer_id) FROM Orders AS O, Charges AS CH WHERE O.date = CH.date AND O.car_id = CH.car_id AND (julianday("now") - O.date)<31')
    all_rows = c.fetchall()
    answer = 'Customer ID\t\tNumber of Charges\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"
    answer8['text'] = answer


def query9():
    c = conn.cursor()
    c.execute(
        'SELECT wid,  part_type_id, MAX(avg_use) FROM '
        '(SELECT wid, part_type_id, AVG(use) AS avg_use FROM'
        '(SELECT CAST(R.date/7 AS INT) AS week, wid, part_type_id, COUNT(*) AS use FROM Repairs AS R GROUP BY wid, part_type_id, CAST(R.date/7 AS INT)) '
        'GROUP BY wid, part_type_id)'
        'GROUP BY wid HAVING MAX(avg_use)')
    all_rows = c.fetchall()
    answer = 'Workshop ID\t\tPart Type ID\t\tAmount pet week\n\t\t'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t\t'
        answer += "\n\t\t"
    answer9['text'] = answer


def query10():
    c = conn.cursor()
    c.execute(
        'SELECT C.car_type_id, AVG(R.AvgRcost + Ch.AvgCHcost) FROM Cars AS C, '
        '(SELECT car_id, AVG(Rcost) AS AvgRcost FROM (SELECT car_id, SUM(cost) AS Rcost, Re.date FROM Repairs AS Re GROUP BY car_id, Re.date ) GROUP BY car_id) AS R, '
        '(SELECT car_id, AVG(CHcost) AS AvgCHcost FROM (SELECT  car_id, SUM(cost) AS CHcost, CHa.date FROM Charges AS CHa GROUP BY car_id, Cha.date) GROUP BY car_id) AS CH '
        ' WHERE C.car_id = R.car_id AND C.car_id = CH.car_id GROUP BY C.car_type_id ORDER BY AVG(R.AvgRcost + Ch.AvgCHcost) DESC LIMIT 1')
    all_rows = c.fetchall()
    answer = 'Car Type ID\t\tTotal cost\n'
    for row in all_rows:
        for item in row:
            answer += str(item) + '\t\t'
        answer += "\n"
    answer10['text'] = answer


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
      text='A customer claims she forgot her bag in a car and asks to help.\nShe was using cars several times this day, but she believes the right car was red and its plate starts with “AN”. ').pack()
Button(q1, text='Run query', command=lambda: query1()).pack()
Button(q1, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer1 = Label(q1, text="  ")
answer1.pack()

# q2 frame input: date
Label(q2, text='Compute how many sockets were occupied each hour.\nPlease enter input date').pack()
input2 = Entry(q2)
input2.pack()
Button(q2, text='Run query', command=lambda: query2(input2.get())).pack()
Button(q2, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer2 = Label(q2, text="")
answer2.pack()

# q3 frame no input
Label(q3, text='Gather statistics for one week on \n how many cars are busy (% to the total amount of taxis)\n').pack()
Button(q3, text='Run query', command=lambda: query3()).pack()
Button(q3, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer3 = Label(q3, text="")
answer3.pack()

# q4 frame
Label(q4, text='Find duplicating payments\n').pack()
Button(q4, text='Run query', command=lambda: query4()).pack()
Button(q4, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer4 = Label(q4, text="")
answer4.pack()

# q5 frame
input5= Entry(q5)
input5.pack()
Label(q5, text='Enter date to get statistics on \n Average distance and Average trip duration \n').pack()
Button(q5, text='Run query', command=lambda: query5(input5.get())).pack()
Button(q5, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer5 = Label(q5, text="")
answer5.pack()

# q6 frame
Label(q6, text='Compute top-3 most popular pick-up locations\n').pack()
Button(q6, text='Run query', command=lambda: query6()).pack()
Button(q6, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer6 = Label(q6, text="")
answer6.pack()

# q7 frame
Label(q7, text='Find 10% of cars which take least amount of\n orders for the last 3 months\n').pack()
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
Label(q9, text='Find parts which are used the most\n every week by every workshop\n').pack()
Button(q9, text='Run query', command=lambda: query9()).pack()
Button(q9, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer9 = Label(q9, text="")
answer9.pack()

# q10 frame
Label(q10, text='Find car type which had the highest average (per day) cost of\n repairs andcharging (combined)\n').pack()
Button(q10, text='Run query', command=lambda: query10()).pack()
Button(q10, text='Back to menu', command=lambda: raise_frame(initial)).pack()
answer10 = Label(q10, text="")
answer10.pack()

raise_frame(initial)
root.mainloop()

import sqlite3
import tkinter as tk
mainWindow=tk.Tk()
mainWindow.title('semple window')
heading_label=tk.Label(mainWindow,text='enter student name')
heading_label.pack()
name_feild=tk.Entry(mainWindow)
name_feild.pack()
heading_label=tk.Label(mainWindow,text='enter student college')
heading_label.pack()
name_feild=tk.Entry(mainWindow)
name_feild.pack()
heading_label=tk.Label(mainWindow,text='enter student address')
heading_label.pack()
name_feild=tk.Entry(mainWindow)
name_feild.pack()
heading_label=tk.Label(mainWindow,text='enter student phone_number')
heading_label.pack()
name_feild=tk.Entry(mainWindow)
name_feild.pack()

def takeValueInput():
    name=name_feild.get()
    print(name)
button=tk.Button(mainWindow,text='save',command=lambda :takeValueInput)
button.pack()
mainWindow.mainloop()
connection=sqlite3.connect('student.db')
print('database open successfully')
TABLE_NAME="student_table"
STUDENT_ID="student_id"
STUDENT_NAME="student_name"
STUDENT_COLLEGE="student_college"
STUDENT_ADDRESS="student_address"
STUDENT_PHONE="student_phone"
connection.execute(" CREATE TABLE IF NOT EXISTS "
                   +  TABLE_NAME +
                   " ( " +  STUDENT_ID +
                   " INTEGER PRIMARY KEY "
                   " AUTOINCREMENT , " +
                   STUDENT_NAME + " TEXT, " +
                   STUDENT_COLLEGE +
                   " TEXT, " +
                   STUDENT_ADDRESS + " TEXT , " +
                   STUDENT_PHONE +
                   " INTEGER) ;")
print('table created successfully.')
connection.execute(" INSERT INTO " + TABLE_NAME +
                   " ( " +
                   STUDENT_NAME + ", " +
                   STUDENT_COLLEGE + ", " +
                   STUDENT_ADDRESS +
                   ", " + STUDENT_PHONE +
                   " ) VALUES ( 'GURJAS', 'DIT', "
                   +
                "'kAPURTHAlA, PUNJAB',987455626 ); ")
connection.commit()

cursor=connection.execute("SELECT * FROM " +
                          TABLE_NAME + " ;")
for row in cursor:
    print("studenet id is :",row[0])
    print("student name is:",row[1])
    print("student college is:",row[2])
connection.close()
name=input('enter your name')
college=input('enter your college')
address=input('enter your address')
phone=input('enter your phone number')

connection.execute(" INSERT INTO " + TABLE_NAME +
                   " ( " +
                   STUDENT_NAME + ", " +
                   STUDENT_COLLEGE + ", " +
                   STUDENT_ADDRESS +
                   ", " + STUDENT_PHONE +
                   " ) VALUES ( '" +name +"', '" +college +"', "
                   + " '"+address +"', "
                   +phone + ");")
connection.commit()
cursor=connection.execute("SELECT * FROM " +
                          TABLE_NAME + " ;")
for row in cursor:
    print("studenet id is :",row[0])
    print("student name is:",row[1])
    print("student college is:",row[2])
    print("student address is:",row[3])
    print("student phone number is:",row[4])
connection.close()




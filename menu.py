#   --Function to display menu for EMS --

import csv
import pyodbc as odbccon
import os
from pprint import pprint
import pickle

# connection to database

conn = odbccon.connect("Driver={SQL Server Native Client 11.0};"
                       "Server=LAPTOP-3D1J4GB8;"
                       "Database=ems;"
                       "Trusted_Connection=yes;")

cursor = conn.cursor()

def mainmenu():
    print("----Welcome to Employee Management System----")
    print("Select your choice to ")
    print("1. Add employee")
    print("2. Remove employee")
    print("3. Display employee")
    print("4.Exit")

    #--- taking choice from user
    ch = int(input("Enter your choice:  "))
    if ch ==1:
        add_employee()
    elif ch==2:
        remove_employee()
    elif ch==3:
        display_employee()
    elif ch==4:
        displayCSV_Data()
        exit()
    else:
        print("Invalid choice")
        mainmenu()


def add_employee():
    id = (input("Enter employee Id in (1XX) format : "))
   
    #-- check if employee already exists
    if (check_employee(id)) == True:
        print("Employee already exists")
        mainmenu()
    else:
        name = input("Enter employee name: ")
        age = input("Enter employee age: ")
        salary = input("Enter salary: ")
        department_id = input("Enter department id: ")
        address_id =input("Enter address id: ")
        manager_id =input("Enter manager id: ")

        # Inserting Employee details in the Employee
        sql = "insert into employee (id ,name,age,salary,department_id,address_id,manager_id) values(?,?,?,?,?,?,?);"
        data = (id ,name,age,salary,department_id,address_id,manager_id)
   
    
        # Executing the SQL Query    
        cursor.execute(sql,data)
 
        # commit() method to make changes in the table
        conn.commit()
        print("Employee Added Successfully ")
        mainmenu()


def remove_employee():
    id = input("Enter employee id: ")

    #- check if employee exists or not
    if(check_employee(id) == True):
        print("Employee does not exist")
        mainmenu()
    else:
        #-query to remove employee from table
        sql = 'delete from employee where id = ?'
        data = (id,)
        c = cursor(buffered=True)

        #execute sql query
        c.execute(sql, data)

        conn.commit()
        print("Employee removed")
        mainmenu()

def check_employee(e_id):
     
    # Query to select all Rows f
    # rom employee Table

    sql = 'select * from employee where id=?'
     
    cursor = conn.cursor()
    data = (id,)
    #data = [e_id,]
     
    # Executing the SQL Query
    cursor.execute('select * from employee where id=?')
   
    # rowcount method to find
    # number of rows with given values
    r = cursor.rowcount
    if r == 1:
        return True
    else:
        return False


def display_employee():
    # query to select all rows from
    # Employee Table
    sql = 'select * from employee'
    c = conn.cursor()
     
    # Executing the SQL Query
    c.execute(sql)
     
    # Fetching all details of all the
    # Employees
    r = c.fetchall()
    for i in r:
        print("Employee id : ", i[0])
        print("Employee name: ", i[1])
        print("Employee age: ", i[2])
        print("Employee salary: ",i[3])
        print("Department_id: ",i[4])
        print("Address id: ", i[5])
        print("Manager_id: ", i[6])
        print("***********************************")
    mainmenu()

#-- import data from csv file
def displayCSV_Data():
    
    rows = []
    try: 
      with open('emp.csv', 'rt', newline ='\n') as csv_file:
        csvreader = csv.reader(csv_file)
        header = next(csvreader)
        rows=next(csvreader)
        for row in csvreader:
            rows.append(row)
            
    except FileNotFoundError: print("File not found")

    print(header)
    print('\n',rows,'\n')
mainmenu()
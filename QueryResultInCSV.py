#----------------Export the results of the SQL queries to CSV file-------------

import csv
import pyodbc as odbccon


# connection to database
conn = odbccon.connect("Driver={SQL Server Native Client 11.0};"
                       "Server=LAPTOP-3D1J4GB8;"
                       "Database=ems;"
                       "Trusted_Connection=yes;")
c = conn.cursor()


#full data for each employee with address as a string, dept_name and mngr_name
sql1 = "select em.id, em.name , em.salary, a.street +'' + a.city as 'full_address', d.name as 'dept_name',mngr.name from employee em full join employee mngr on (em.manager_id = mngr.id) join department d on (em.department_id = d.id) join address a on (d.headquarter_address_id = a.id);"
c.execute(sql1)
res1 = c.fetchall()


 # for top 5 highest paid salary    
sql2 = "select top 5 id, name, salary from employee where salary <= (select max(salary) from employee)  order by salary desc;"
c.execute(sql2)
res2 = c.fetchall()

# for top 5 lowest paid salary 
sql3 = "select top 5 id, name, salary from employee where salary >= (select min(salary) from employee) order by salary; "
c.execute(sql3)  
res3 = c.fetchall()

# for the total salary for each department, the manager's name, sorted by highest total
sql4 = "select d.id, sum(e.salary) as 'Total_salary_each_dept.' from department d join employee e on (d.id= e.department_id) group by d.id order by 'Total_salary_each_dept.'desc;"
c.execute(sql4)
res4 = c.fetchall()

# for each employee that lives in a given state 
sql5 = "select e.name,a.state from employee e join address a on (a.id = e.address_id) where a.state = 'Texas';"
c.execute(sql5)
res5 = c.fetchall()

#just to separate two result add newline and some dash
a1 = ["------------FULL DATA WITH ADDRESS AS A STRING, DEPT_name & MANAGER_NAME-----------"]
a2 = ["                   \t"]
a3 = ["-----------HIGHEST PAID SALARIES--------"]
a4 = ["                 \t"]
a5 = ["---------LOWEST PAID SALARIES--------- "] 
a6 = ["                  \t"]
a7 = ["---------TOTAL SALARY FOR DEPT. SORTED BY HIGHEST---------"]
a8 = ["                   \t"]
a9 = ["---------EMPLOYEE THAT LIVES IN TEXAS----------"]
a10 = ["                    \t"]
   
#export to csv
with open("query_2.csv","w", newline='') as csv_file:
    csv.writer(csv_file).writerow(a1)
    for row in res1:
        csv.writer(csv_file).writerow(row)
    csv.writer(csv_file).writerow(a2)
    csv.writer(csv_file).writerow(a3)

    for row in res2:
        csv.writer(csv_file).writerow(row)
    csv.writer(csv_file).writerow(a4)
    csv.writer(csv_file).writerow(a5)

    for row in res3:
        csv.writer(csv_file).writerow(row)
    csv.writer(csv_file).writerow(a6)
    csv.writer(csv_file).writerow(a7)

    
    for row in res4:
        csv.writer(csv_file).writerow(row)
    csv.writer(csv_file).writerow(a8)
    csv.writer(csv_file).writerow(a9)

    
    for row in res5:
        csv.writer(csv_file).writerow(row)
    csv.writer(csv_file).writerow(a10)
    

c.close()

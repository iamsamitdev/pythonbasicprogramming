import util.connectMySQL as con

connection = con.getConnection()

sql = "Select Emp_No, Emp_Name, Hire_Date from Employee " \
      "Where Dept_Id = %s"

try:
    cursor = connection.cursor()
    cursor.execute(sql, (20))

    for row in cursor:
        print(" ----------- ")
        #print("Row: ", row)
        print("Emp_No: ", row["Emp_No"])
        print("Emp_Name: ", row["Emp_Name"])
        print("Hire_Date: ",row["Hire_Date"], row["Hire_Date"])
finally:
    connection.close()


import util.connectMySQL as con

connection = con.getConnection()

try:
    cursor = connection.cursor()
    sql = "INSERT INTO employee " \
          "(EMP_ID, EMP_NAME, EMP_NO, HIRE_DATE, JOB, SALARY, DEPT_ID) " \
          "values (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(sql, (8000, "Samit", "E8000", "2020-12-17", "Programmer", "30000", "20"))
    connection.commit()
    print("Add new employee success")
finally:
    connection.close()
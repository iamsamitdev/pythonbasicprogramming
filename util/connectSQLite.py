import sqlite3

conn = sqlite3.connect('../db/companydb.db')
c = conn.cursor()

# Insert
# Insert a row of data
c.execute("INSERT INTO employee VALUES (NULL,'Johny','john@gmail.com','25000')")
# Save (commit) the changes
conn.commit()

# Read
resut = c.execute("SELECT * FROM employee")
for row in resut:
    print(row[1], row[2], row[3])

# Update
c.execute("UPDATE employee SET fullname='Wichai', email='wichai@gmail.com' WHERE id = 2")
conn.commit()

# Delete
c.execute("DELETE FROM employee WHERE id >= 3")
conn.commit()
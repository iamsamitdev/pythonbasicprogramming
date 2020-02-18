import pymysql.cursors

def getConnection():
    # Connect to the database
    host = "192.168.1.41"
    user = "root"
    password = "1234"
    dbname = "companydb"
    charset = "utf8"

    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=dbname,
        charset=charset,
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# print(getConnection())
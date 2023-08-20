'''
A Script that list all users in the table
'''

# import dbobject
import MySQLdb

# try connection and execution 
try:
    # connect to database
    database = MySQLdb.connect(user="root", passwd="root", db="?")

    # set cursor if connection succed
    cursor = database.cursor()

    # run the select statement on the states table
    cursor.execute("SELECT * FROM states ORDER by states.id")

    # fetch all rows in the result
    rows = cursor.fetchall()

    # loop through the result to get the state id and name
    for row in rows:
        print(row)

#   if there is an error catch it with and exception message
except MySQLdb.OperationalError as e:
    
    # print the error message
    print("Connection failed. {}".format(e))

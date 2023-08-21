'''
This module is for task 1 which filter states using the
Keyword 'N'.
The User pass the param through the terminal and the value is obtained
using the argV  and the db is querried with the param N

'''

# import dbobject
import MySQLdb
import sys

# try connection and execution
try:
    # connect to database

    if len(sys.argv) > 3:
        database = MySQLdb.connect(user=f"{sys.argv[1]}",

                                   passwd=f"{sys.argv[2]}",
                                   db=f"{sys.argv[3]}")

        # set cursor if connection succed
        cursor = database.cursor()

        # run the select statement on the states table where users name start
        # with N using the like operation.
        cursor.execute("SELECT * FROM states WHERE name =\
                        'N%' ORDER by states.id")

        # fetch all rows in the result
        rows = cursor.fetchall()

        # loop through the result to get the state id and name
        for row in rows:
            print(row)
    else:
        pass

    # if there is an error catch it with and exception message
except MySQLdb.OperationalError as e:

    # print the error message
    print("Connection failed. {}".format(e))

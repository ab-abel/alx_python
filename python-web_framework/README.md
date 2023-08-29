# Python - Web framework
- General
    - What is a Web Framework
    - How to build a web framework with Flask
    - How to define routes in Flask
    - What is a route
    - How to handle variables in a route
    - What is a template
    - =How to create a HTML response in Flask by using a template
    - How to create a dynamic template (loops, conditions…)
    - How to display in HTML data from a MySQL database
# ALL TASK

## Task 0
###  Hello Flask!
Write a script that starts a Flask web application:

    - Your web application must be    listening on 0.0.0.0, port 5000
    Routes:
        - /: display “Hello HBNB!”
    - You must use the option strict_slashes=False in your route definition

## Task 1
###  HBNB
Copy the previous task to a new script that starts a Flask web application:

    - Your web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display “HBNB”
    - You must use the option strict_slashes=False in your route definition

## Task 2
###  C is fun!
Copy the previous task to a new script that starts a Flask web application:

    - Your web application must be listening on 0.0.0.0, port 5000
    - Routes:
        - /: display “Hello HBNB!”
        - /hbnb: display “HBNB”
        - /c/<text>: display “C ” followed by the value of the text variable (replace underscore _ symbols with a space )
    - You must use the option strict_slashes=False in your route definition
## Task 3
###   SQL Injection...
    Wait, do you remember the previous task? Did you test "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" as an input?
    
    guillaume@ubuntu:~/$ ./2-my_filter_states.py root root hbtn_0e_0_usa "Arizona'; TRUNCATE TABLE states ; SELECT * FROM states WHERE name = '" (2, 'Arizona')
    guillaume@ubuntu:~/$ ./0-select_states.py root root hbtn_0e_0_usa
    guillaume@ubuntu:~/$ 

        What? Empty?

        Yes, it’s an SQL injection to delete all records of a table…

        Once again, write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!

        - Your script should take 4 arguments: mysql username, mysql password, database name and state name searched (safe from MySQL injection)
        - You must use the module MySQLdb (import MySQLdb)
        - Your script should connect to a MySQL server running on localhost at port 3306
        Results must be sorted in ascending order by states.id
        - Results must be displayed as they are in the example below
        - Your code should not be executed when imported
## Task 4
### Cities by states
    Write a script that lists all cities from the database hbtn_0e_4_usa

        - Your script should take 3 arguments: mysql username, mysql password and database name
        - You must use the module MySQLdb (import MySQLdb)
        - Your script should connect to a MySQL server running on localhost at port 3306
        - Results must be sorted in ascending order by cities.id
        - You can use only execute() once
        - Results must be displayed as they are in the example below
        - Your code should not be executed when imported


## Task 5
### All cities by state
    Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa

        - Your script should take 4 arguments: mysql username, mysql password, database name and state name (SQL injection free!)
        - You must use the module MySQLdb (import MySQLdb)
        - Your script should connect to a MySQL server running on localhost at port 3306
        - Results must be sorted in ascending order by cities.id
        - You can use only execute() once
        - The results must be displayed as they are in the example below
        - Your code should not be executed when imported
## Task 6
### First state model
    Write a python file that contains the class definition of a State and an instance Base = declarative_base():

        - State class:
            - inherits from Base Tips
            - links to the MySQL table states
            - class attribute id that represents a column of an auto-generated, unique integer, can’t be null and is a primary key
            - class attribute name that represents a column of a string with maximum 128 characters and can’t be null
        - You must use the module SQLAlchemy
        - Your script should connect to a MySQL server running on localhost at port 3306
###     WARNING: 
        all classes who inherit from Base must be imported before calling Base.metadata.create_all(engine)
## Task 7
### All states via SQLAlchemy
    Write a script that lists all State objects from the database hbtn_0e_6_usa

        - Your script should take 3 arguments: mysql username, mysql password and database name
        - You must use the module SQLAlchemy
        - You must import State and Base from model_state - from model_state import Base, State
        - Your script should connect to a MySQL server running on localhost at port 3306
        - Results must be sorted in ascending order by states.id
        - The results must be displayed as they are in the example below
        - Your code should not be executed when imported
## Task 8
###  First state
    Write a script that prints the first State object from the database hbtn_0e_6_usa        
        - Your script should take 3 arguments: mysql username, mysql password and database name
        - You must use the module SQLAlchemy
        - You must import State and Base from model_state - from model_state import Base, State
        - Your script should connect to a MySQL server running on localhost at port 3306
        - The state you display must be the first in states.id
        - You are not allowed to fetch all states from the database before displaying the result
        - The results must be displayed as they are in the example below
        - If the table states is empty, print Nothing followed by a new line
        - Your code should not be executed when imported

## Task 9
### Contains `a`
    Write a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa

        - Your script should take 3 arguments: mysql username, mysql password and database name
        - You must use the module SQLAlchemy
        - You must import State and Base from model_state - from model_state import Base, State
        - Your script should connect to a MySQL server running on localhost at port 3306
        - Results must be sorted in ascending order by states.id
        - The results must be displayed as they are in the example below
        - Your code should not be executed when imported
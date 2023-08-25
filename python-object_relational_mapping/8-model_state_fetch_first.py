'''
Write a script that lists all State objects
from the database hbtn_0e_6_usa
'''
# Import Modules from ORM
from sqlalchemy import create_engine, select
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# import Base and table from model
from model_state import Base, State


# import sys to get values from terminal
import sys

# import session for database interraction
from sqlalchemy.orm import sessionmaker

# define Base class for table class inheritance
try:
    # create a DB engine connection
    engine = create_engine(
                           "mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # create a session variable and bint the engine to it
    Session = sessionmaker(bind=engine)

    # instatiate the session
    session = Session()

    results = session.query(State).first()

    print(f"{results.id}: {results.name}")
except AttributeError as e:
    print(f"error message {e}")

except sqlalchemy.exc.ProgrammingError as e:
    print(f"An Error occured: {e}")

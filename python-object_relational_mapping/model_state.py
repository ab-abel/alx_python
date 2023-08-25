'''
Write a python file that contains the class definition of a State
and an instance Base = declarative_base()
'''
# Import Modules from ORM
from sqlalchemy import create_engine, Column, Integer, String
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

# define Base class for table class inheritance
Base = declarative_base()


# create a table for class state
class State(Base):
    '''
        class defintion for SQL table states
        pARAMETER
            Base declarative
        Return:
        base meta data for the creation of state tables
    '''
    # define table name
    __tablename__ = 'states'
    # define column for states table
    id = Column(Integer, primary_key=True,
                autoincrement=True, unique=True, nullable=False)
    name = Column(String(128), nullable=False)

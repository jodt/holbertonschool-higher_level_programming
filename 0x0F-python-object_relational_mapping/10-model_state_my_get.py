#!/usr/bin/python3
"""
This is the model_state_my_get module that
rints the State object with the name passed as argument
from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)
    result = session.query(State).filter(
        State.name == sys.argv[4]).one_or_none()
    print(result.id if result else 'Not found')
    session.close()

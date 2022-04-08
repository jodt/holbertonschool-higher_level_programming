#!/usr/bin/python3
"""
This is the model_state_update module that
changes the name of a State object from the database
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
    element = session.query(State).get(2)
    element.name = "New Mexico"
    session.commit()
    session.close()

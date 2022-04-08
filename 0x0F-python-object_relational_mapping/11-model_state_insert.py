#!/usr/bin/python3
"""
This is the model_state_insert that
adds the State object “Louisiana” to the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
if __name__ == "__main__":
    new_state = State(name='Louisiana')
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)
    session.add(new_state)
    session.commit()
    print(new_state.id)
    session.close()

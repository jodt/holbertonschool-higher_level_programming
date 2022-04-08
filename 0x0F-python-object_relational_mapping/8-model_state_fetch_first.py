#!/usr/bin/python3
"""
This is the model_state_fetch_first that
prints the first State object from the database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)
    row = session.query(State).first()
    print("{}: {}".format(row.id, row.name) if row else "Nothing")
    session.close()

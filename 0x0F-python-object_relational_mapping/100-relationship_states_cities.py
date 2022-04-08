#!/usr/bin/python3
"""
This is the relationship_states_cities
"""
from os import stat_result
import sys
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost/{}".format(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3]),
        pool_pre_ping=True)
    session = Session(engine)
    Base.metadata.create_all(engine)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()

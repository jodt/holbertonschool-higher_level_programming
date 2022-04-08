#!/usr/bin/python3
"""
This is therelationship_cities_states_list
that lists lists all City objects from the database"""

import sys
from relationship_city import City
from relationship_state import Base, State
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
    for city, state in session.query(
        City, State).filter(
        City.state_id == State.id).order_by(
            City.id).all():
        print("{}: {} -> {}".format(city.id, city.name, state.name))
    session.close()

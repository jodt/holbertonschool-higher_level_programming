#!/usr/bin/python3
"""
This is the relationship_states_cities_list
that lists all State objects, and corresponding
City objects, contained in the database
"""
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
    list_result = session.query(State).join(City).filter(
        State.id == City.state_id).order_by(
        State.id).order_by(
        City.id).all()
    for state in list_result:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
    session.close()

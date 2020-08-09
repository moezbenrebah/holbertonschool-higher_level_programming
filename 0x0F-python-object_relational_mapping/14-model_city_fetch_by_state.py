#!/usr/bin/python3
"""
a script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":

    eng = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(eng)
    S = sessionmaker(bind=eng)
    session = S()
    rows = session.query(City, State).filter(City.state_id == State.id).all()
    for city, state in rows:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.commit()
    session.close()

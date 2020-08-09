#!/usr/bin/python3
"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import State


if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                        .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                        pool_pre_ping=True)

    S = sessionmaker(bind=eng)
    session = S()

    for state in session.query(State).order_by(State.id):
        print("{}: {}".format(state.id, state.name))

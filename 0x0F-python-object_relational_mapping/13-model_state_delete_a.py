#!/usr/bin/python3
"""Script to delete State objects from the database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    # Query and delete State objects with names containing 'a'
    states_with_a = session.query(State).filter(State.name.like('%a%')).all()
    for state in states_with_a:
        session.delete(state)

    session.commit()
    session.close()

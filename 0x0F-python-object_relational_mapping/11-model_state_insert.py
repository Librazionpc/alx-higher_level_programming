#!/usr/bin/python3
"""Scripts that adds to the database
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
    new_state_name = "Louisiana"

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, database))

    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name=new_state_name)

    session.add(new_state)

    session.commit()
    state = session.query(State).filter_by(name=new_state_name).first()
    if state:
        print(state.id)
    else:
        print("Nothing")

    session.close()

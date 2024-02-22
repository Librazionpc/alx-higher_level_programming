#!/usr/bin/python3
"""Class definition for city"""
import sys
from sqlalchemy import (create_engine)
from model_city import City, Base
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

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))

    session.close()

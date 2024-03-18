#!/usr/bin/python3
"""Filters Ctes in the database
"""
import sys
import MySQLdb

if __name__ == '__main__':
    if len(sys.argv) != 5:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306
        )

        cursor = db.cursor()
        qury = "SELECT cities.name FROM cities JOIN states ON cities.state_id"\
            " = states.id WHERE states.name = %s ORDER BY cities.id ASC"
        cursor.execute(qury, (state_name,))
        cities = cursor.fetchall()

        cities_names = [city[0] for city in cities]
        print(", ".join(cities_names))

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

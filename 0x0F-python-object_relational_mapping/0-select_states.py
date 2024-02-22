#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=username,
            passwd=password,
            db=database,
            port=3306)
        cursor = db.cursor()

        cursor.execute("SELECT * FROM states ORDER BY id ASC")
        states = cursor.fetchall()

        for state in states:
            print(state)

        cursor.close()
        db.close()

    except MySQLdb.Error as e:
        print("MySQL Error {}: {}".format(e.args[0], e.args[1]))
        sys.exit(1)

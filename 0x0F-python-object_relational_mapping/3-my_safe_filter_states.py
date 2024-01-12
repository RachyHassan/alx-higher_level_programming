#!/usr/bin/python3
""" A script that lists all states from the database hbtn_0e_0_usa,
while also bypassing SQL injections. """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         db=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    match = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

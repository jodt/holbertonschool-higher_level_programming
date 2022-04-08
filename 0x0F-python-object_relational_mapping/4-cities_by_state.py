#!/usr/bin/python3
"""
This is the cities_by_state module
"""
import MySQLdb
import sys
if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8")
    cur = db.cursor()
    cur.execute(
        "SELECT cities.id, cities.name, states.name FROM cities \
INNER JOIN states ON states.id=cities.state_id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()

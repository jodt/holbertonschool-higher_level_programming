#!/usr/bin/python3
"""
This is the filter_cities module
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
    cur.execute("SELECT cities.name FROM cities \
INNER JOIN states ON states.id=cities.state_id \
WHERE states.name = %s ORDER BY cities.id", (sys.argv[4],))
    rows = cur.fetchall()
    list = []
    for row in rows:
        list.append(row[0])
    print(', '.join(list))
    cur.close()
    db.close()

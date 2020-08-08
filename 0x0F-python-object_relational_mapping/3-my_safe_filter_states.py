#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys

if __name__ == '__main__':
    argument = sys.argv[4]
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("""SELECT cities.name
                FROM cities JOIN states
                ON cities.state_id = states.id
                WHERE states.name = %s
                ORDER BY cities.id ASC;""", (argument,))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))

    cur.close()
    db.close()

import os
import datetime
import pymysql

# Get username from Cloud9 workspace
# (modify this variable if running on another environment)
username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a query
    with connection.cursor(pymysql.cursors.DictCursor) as cursor:
        rows = cursor.executemany("DELETE FROM Friends WHERE name = %s;", ['Bob', 'Fred'])
        connection.commit()
        for row in cursor:
            print(row)
finally:
    # Close the connection, regardless of whether or not the above was successfull
    connection.close()
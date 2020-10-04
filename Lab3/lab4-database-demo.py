#!/usr/bin/env python3
import sqlite3
#connect to database file
dbconnect = sqlite3.connect("mydatabase.db");
#If we want to access columns by name we need to set
#row_factory to sqlite3.Row class
dbconnect.row_factory = sqlite3.Row;
#now we create a cursor to work with db
cursor = dbconnect.cursor();

#print data

print('\nDisplaying all the sensors in the kitchen...')
cursor.execute('SELECT * FROM sensors WHERE zone="kitchen"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
    
print('\nDisplaying all the door sensors...')
cursor.execute('SELECT * FROM sensors WHERE type="door"');
for row in cursor:
    print(row['sensorID'],row['type'],row['zone']);
    
#close the connection
dbconnect.close();

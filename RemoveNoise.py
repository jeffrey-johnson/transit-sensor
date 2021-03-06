"""REMOVE SQL ENTRIES FROM ADDRESS_LIST"""

import MySQLdb
from datetime import datetime

"""Connect to database"""
def connectDB():
   db = MySQLdb.connect(host='localhost',
		     user='root',
		     passwd='Toh6Woeg',
		     db='TransitSensor')
   cursor = db.cursor()
   return db, cursor

"""Delete unique addresses, this removes any address that wasnt picked up a second time"""
def deleteUnique(db,cursor):
   cursor.execute('DELETE FROM Timestamps WHERE address IN ( SELECT * FROM ( SELECT address FROM Timestamps GROUP BY address HAVING (COUNT(*) = 1)) AS p )')
   db.commit()

"""Printing function to see the table"""
def printTimestamp(cursor):
   cursor.execute("SELECT time, address FROM Timestamps")
   for row in cursor.fetchall():
      print row

"""Deletes non unique addresses with a time of riding under 2 minutes
   Gets the first and last appearence of the rider, gets the time difference
   and deletes it if it is under 2 minutes"""
def deleteUnderThreshold(db,cursor):
   cursor.execute('SELECT time, address FROM Timestamps WHERE address IN (SELECT address FROM Timestamps Group By address having count(*) != 1)')
   timestamps = []
   addresses = []
   time_difference = []
   address_list = []
   for row in cursor.fetchall():
      timestamps.append(row[0])
      addresses.append(row[1])
   for i in range(len(timestamps)):
	min_time = timestamps[i]
	min_addr = addresses[i]
        print "min_time staring is {}, min_addr is{}".format(min_time, min_addr)
	print len(timestamps), i
	for j in range(len(timestamps)):
	   if addresses[j] != addresses[i] or j+1 >= len(timestamps):
	      address_list.append(addresses[j-1])
	      print timestamps[j-1],  min_time, addresses[j-1]
	      time_difference.append(timestamps[j-1] - min_time)
	      i = j
	      min_time = timestamps[i]
        if addresses[i] == addresses[-1]:
	   break
   deletes = []
   for i in range(len(address_list)):
      print address_list[i], time_difference[i].total_seconds() < 120
      if time_difference[i].total_seconds() < 120:
	 deletes.append(address_list[i])
   print deletes
   for i in deletes:
      cursor.execute("DELETE FROM Timestamps WHERE address = (%s)",[i])
   db.commit() 

"""Closes the database"""
def closeDB(db,cursor):
   cursor.close()
   db.close()

"""main function to call the others"""
if __name__ == '__main__' :
   db, cursor = connectDB()
   printTimestamp(cursor)
   deleteUnderThreshold(db,cursor)
   printTimestamp(cursor)
   deleteUnique(db,cursor)
   closeDB(db,cursor)

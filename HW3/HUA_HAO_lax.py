import sys
DA=sys.argv[1]
year=sys.argv[2]

import mysql.connector
cnx = mysql.connector.connect(user='inf551', password='inf551',
host='127.0.0.1', database='inf551')
cursor=cnx.cursor()

sql="SELECT SUM(passenger_count) AS SUM_passenger FROM LAX WHERE arrv_dept IN ('%s') AND YEAR(report_period) IN ('%s')" % (DA,year)
cursor.execute(sql)

for SUM_passenger in cursor:
    print SUM_passenger

cursor.close()
cnx.close()

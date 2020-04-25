
# 2017.03.10 INF551 HW3
# HUA HAO

import mysql.connector
cnx = mysql.connector.connect(user='inf551', password='inf551',
host='127.0.0.1', database='inf551')
cursor=cnx.cursor()

import json
import sys

#there should be some codes tell python where the lax.json file was stored.
#import os
#os.chdir('/home/ec2-user/inf551/data')

f=open(sys.argv[1])
#f=open('/home/ec2-user/inf551/data/lax.json')
lax=json.load(f)
report_period=[]
terminal=[]
arrv_dept=[]
dom_inter=[]
passenger_count=[]
for i in lax["data"]:
        report_period.append(i[9])
        terminal.append(i[10])
        arrv_dept.append(i[11])
        dom_inter.append(i[12])
        passenger_count.append(i[13])
passenger_count=[float(x) for x in passenger_count]
junk1=[x[0:10] for x in report_period]
junk2=[x[11:19] for x in report_period]
junk3=["%s %s"% t for t in zip(junk1,junk2)] 
f='%Y-%m-%d %H:%M:%S'

import datetime
junk=[]
for i in range(0,4812):
        junk.append(datetime.datetime.strptime(junk3[i], f))
report_period=junk

for i in range(0,4812):
        report_period_r=report_period[i]
        terminal_r=terminal[i]
        arrv_dept_r=arrv_dept[i]
        dom_inter_r=dom_inter[i]
        passenger_count_r=passenger_count[i]
        sql="insert into LAX (report_period, terminal, arrv_dept, dom_inter, passenger_count) values ('%s', '%s','%s','%s','%d')" %(report_period_r, terminal_r, arrv_dept_r, dom_inter_r, passenger_count_r)
        cursor.execute(sql)

cnx.commit()

cursor.close()
cnx.close()

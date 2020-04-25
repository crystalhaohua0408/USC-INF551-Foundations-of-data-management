import boto3
from boto.dynamodb2.table import Table
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

dynamodb=boto3.resource('dynamodb')
table=dynamodb.Table('hw4_lax2')

import sys

#fe=Attr('arrv_dept').eq('Departure') & Attr('Year').eq(2015)
fe=Attr('arrv_dept').eq(sys.argv[1]) & Attr('report_period').begins_with(sys.argv[2])
pe="passenger_count"

response=table.scan(
    FilterExpression=fe,
    ProjectionExpression=pe,
    )

items=response['Items']

length=len(items)

#print(items)
#a=list(items[1].values())
#print(type(a))
#print(a[0])

junk=[]
for i in range(length-1):
    a=list(items[i].values())
    junk.append(a[0])

total=0
for i in junk:
    total +=i
print(total)

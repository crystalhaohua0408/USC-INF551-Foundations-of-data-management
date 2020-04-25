import boto3
dynamodb = boto3.resource('dynamodb')

table=dynamodb.create_table(
    TableName='hw4_7',
    KeySchema=[
        {
            'AttributeName': 'record_id',
            'KeyType': 'HASH'
        },
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'record_id',
            'AttributeType': 'N'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)

# Wait until the table exists.
table.meta.client.get_waiter('table_exists').wait(TableName='hw4_7')
print(table.item_count)

table=dynamodb.Table('hw4_7')
print(table.creation_date_time)


import json
import sys

#there should be some codes tell python where the lax.json file was stored.
#import os
#os.chdir('/home/ec2-user/inf551/data')

#f=open(sys.argv[1])
f=open('/home/ec2-user/inf551/data/lax.json')
lax=json.load(f)

record_id=[]
report_period=[]
terminal=[]
arrv_dept=[]
dom_inter=[]
passenger_count=[]
for i in lax["data"]:
    record_id.append(i[0])
    report_period.append(i[9])
    terminal.append(i[10])
    arrv_dept.append(i[11])
    dom_inter.append(i[12])
    passenger_count.append(i[13])

from decimal import *
passenger_count=[Decimal(x) for x in passenger_count]
#year=[Decimal(x) for x in year]

with table.batch_writer() as batch:
    for i in range(1000):
        batch.put_item(
            Item={
                'record_id':record_id[i],
                'report_period':report_period[i],
                'Terminal':terminal[i],
                'arrv_dept':arrv_dept[i],
                'dom_inter':dom_inter[i],
                'passenger_count': passenger_count[i],           
            }
        )

response=table.get_item(
    Key={
        'record_id': 1000
        }
)
item=response['Items']
print(item)





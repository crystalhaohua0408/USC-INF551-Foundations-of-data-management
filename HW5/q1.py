import sys
from pyspark.sql import SparkSession
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("HUA_GIVE_NAME").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

country = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "country").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()
city= spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "city").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()

from operator import add
junk=city.map(lambda x:(x[2],1)).reduceByKey(add)

#create a list of country code whose cities more than 100
mylist=junk.filter(lambda x: x[1]>100).map(lambda x:x[0]).collect
capitals=country.filter(lambda x: x[0] in mylist).map(lambda x: x[13]).collect()
nc=country.filter(lambda x: x[0] in mylist).map(lambda x: (x[13],x[1]))
nc2=city.filter(lambda x:x[0] in capitals).map(lambda x: (x[0],x[1]))
nc3=nc.join(nc2).map(lambda x:x[1]).sortByKey().collect()

print('\n'.join('   '.join(t) for t in nc3))





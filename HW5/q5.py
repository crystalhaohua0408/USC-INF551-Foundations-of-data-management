import sys
from pyspark.sql import SparkSession
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("HUA_GIVE_NAME").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

country = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "country").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()

from operator import add
population=country.map(lambda x: (x[2],x[6]))
cp=population.groupByKey().mapValues(lambda x: sum(x)/len(x)).sortByKey().collect()

resultList = cp
for val in resultList:
   print val[0], '\t', val[1]

import sys
from pyspark.sql import SparkSession
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("HUA_GIVE_NAME").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

country = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "country").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()

gnp=country.map(lambda x: x[8]).max()
junk=country.filter(lambda x:x[8]==gnp).map(lambda x: x[1]).collect()
from __future__ import print_function
print(*junk, sep="\n")

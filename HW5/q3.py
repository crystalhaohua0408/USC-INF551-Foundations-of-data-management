import sys
from pyspark.sql import SparkSession
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("HUA_GIVE_NAME").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

country = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "country").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()
countrylanguage=(spark.read.format("jdbc").option("url","jdbc:mysql://localhost:3306/world").option("dbtable","countrylanguage").option("user","inf551").option("password","inf551").load()).rdd.map(list).persist()

junk=countrylanguage.filter(lambda x:x[1] in ["English","French"] and x[2] in ["T"])
from operator import add
from collections import Counter
counts=Counter(junk.map(lambda x: x[0]).collect())
code=[i for i in counts if counts[i]==2]
junk=country.filter(lambda x: x[0] in code).map(lambda x: x[1]).collect()
from __future__ import print_function
print(*junk, sep="\n")

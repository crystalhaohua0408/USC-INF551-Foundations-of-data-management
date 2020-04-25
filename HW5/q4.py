import sys
from pyspark.sql import SparkSession
reload(sys)
sys.setdefaultencoding('utf-8')

spark = SparkSession.builder.appName("HUA_GIVE_NAME").getOrCreate()
spark.sparkContext.setLogLevel('ERROR')

country = spark.read.format("jdbc").option("url", "jdbc:mysql://localhost:3306/world").option("dbtable", "country").option("user", "inf551").option("password", "inf551").load().rdd.map(list).persist()
countrylanguage=(spark.read.format("jdbc").option("url","jdbc:mysql://localhost:3306/world").option("dbtable","countrylanguage").option("user","inf551").option("password","inf551").load()).rdd.map(list).persist()

junk=countrylanguage.filter(lambda x:x[1] in ["English","French"] and x[2] in ["T"])
junk1=countrylanguage.filter(lambda x:x[2] in ["T"] and x[1] in ["English"])

from operator import add
from collections import Counter
counts=Counter(junk.map(lambda x: x[0]).collect())
counts1=Counter(junk1.map(lambda x: x[0]).collect())
code=[i for i in counts if counts[i]==2]
code1=[i for i in counts1 if counts[i]==1]
code2=list(set(code1)-set(code))

junkjunk=country.filter(lambda x: x[0] in code2).map(lambda x: x[1]).collect()

from __future__ import print_function
print(*junkjunk, sep="\n")

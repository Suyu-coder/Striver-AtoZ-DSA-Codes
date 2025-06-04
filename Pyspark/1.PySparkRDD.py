
# RDD creation 
from pyspark.sql import SparkSession
spark = SparkSession.builder.master('local[1]')\
    .appName('SparkByExample').getOrCreate()

# CREATE a RDD from parallelize
data = [1,2,3,4,5,6,7,8,9,10,11]
rdd = spark.sparkContext.parallelize(data)

#create a RDD from the external dataSources
rdd2 = spark.sparkContext.textFile('Path.txt')

# read entire file into a RDD as single record 
rdd3 = spark.sparkContext.wholeTextFiles('path.txt')

# create an enpty RDD with no partrations 
rdd = spark.sparkContext.emptyRDD

# create empty RDD with partation
rdd2 = spark.sparkContext.parallelize([],10) # this will be create 10 parations 

# Get partations count
print("Initial partationcount" + str(rdd.getNumPartitions()))

# set the partation manually
sparkContext.parallelize([1,3,2,4,6,3,2,4,7],10)

# Repartition
reparRdd = rdd.repartition(4)
print('re-partition count' + str(reparRdd.getNumPartitions()))

# coalesce()
rdd3 = rdd1.coalesce(4)
print("Repartitions size : " + str(rdd3.getNumPartations()))
rdd3.saveAsTextFile('path/coalesce')

## Pyspark RDD Operations

# 1. flatMap()
# split the data by spact anmd flatten it 
rdd2 = rdd.flatMap(lambda x : s.split(" "))

# 2. map() 
# app the map transformation 
# add a new elemet with value 1 to erach word
rdd3 = rdd2.map(lambda x: (x,1))

#3.reduceByKey()
rdd4 = rdd3.reduceByKey(lambda a,b: a+b)

#4.sortByKey()
rdd5 = rdd4.map(lambda x : (x[1],[0])).sortByKey()
print(rdd5.collect())

## RDD Actions with Example

# count()
print("Count :" + str(rdd6.count()))

# first() # return the first record
firstRec = rdd6.first()
print("First Record : " + str(firstRec[0] + ',' + firstRec[1]))

# max
datMax = rdd6.max()

# reduce() this will use for count or sum
totalWordCount = rdd6.reduce(lambda a,b : (a[0] +b[0],a[1]))

# take() return the specific as an argument 
data3 = rdd6.take(3)
for f in data3:
    print("data3 key" + str([f[0]]) + ", value : " + f[1])

# RDD cache()
cachedRdd = rdd.cache()

# RDD Persist
# MEMORY_ONLY, MEMORY_ONLY_SER, MEMORY_AND_DISK, MEMORY_AND_DISK_SER, DISK_ONLY, MEMORY_ONLY_2, MEMORY_AND_DISK_2
import Py_Spark
dfPresist = rdd.persist(pyspark.StorageLevel.MEMORY_ONLY)
dfPresist.show(False)

#RDD Unpersist
rddPersist2 = rddPersist.unpersist()

# Create a broadcast Variable 
broadcastVar = sc.broadcast([0,1,2,3,4])
broadcastVar.value

#Accumulators
# create a axccumulator variable 
accum = sc.longAccumulator('SumAccumulator')
sc.parallelize([1,2,3]).foreach(lambda x : accum.add(x))

# convert RDD to DataFrame
dfFromRDD = rdd.toDf()

# convert RDD to DataFrame with Column names
dfFromRDD2 = rdd.toDf('col1','col2')

# using create DataFrame() - convert dataFrame to RDD 
df = spark.createDataFrame(rdd).toDF('col1','col2')

rdd = df.rdd 


#Pyspark - parallelize 
rdd = sc.paralledlize([1,2,3,4,5,6,7,8,9,10])

import py_Spark 
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('name').getOrCreate()
sparkContext = spark.sparkContext

rdd = sparkContext.parallelize([1,2,3,4,5])
rddCollect = rdd.collect()

print("Number of partation : " + str(rdd.getNumPartations()))
print("Actions : First element" + str(rdd.first ()))
print(rddCollect)


# PySpark RDD Repartition()

# Create spark session with local[5]
rdd = spark.sparkContext.parallelize(range(0,20))
print("From local[5]: " + str(rdd.getNumPartations()))

# Use parallelize with 6 partitions
rdd1 = spark.sparkContext.parallelize(range(0,25),6)
print("parallelize : " + str(rdd1.getNumPartations()))

rddFromFile = spark.sparkContext.textFile("path",10)
print("TextFile : " + str(rddFromFile.getNumPartitions()))

# using repartitions
rdd2 = rdd1.repartition(4)
print("Repartition Size : " + str(rdd2.getNumPartitions()))
rdd2.saveAsTextFile('/temp/re-partition')

#Using Coalesce()
rdd3 = rdd1.coalesce(4)
print("Repartiton Size : " + str(rdd3.getNumPartitiions()))
rdd3.saveAsTextFile('/tmp/coalesce')

#PysparkDataFrame repartition() and Coalesce()

# create DataFrame Example
import PySpark 
from pyspark.sql import SparkSession
spark = SparkSession.builder.appName('SparkName')\
    .master('local[5]').getOrCreate()

df = spark.range(0,20)
print(df.rdd.getNumPartitions())

df.write.mode('Overwrite').csv('path')

# dataframe Repartitions
df2 = df.repartition(6)
print(df2.rdd.getNumPartitions())

#DataFame coalesce
df3 = df.coalesce(2)
print(df3.rdd.getNumPartitions())

# default shuffle partition count
df4 = df.groupBy('id').count()
print(df4.rdd.getNumPartitions())

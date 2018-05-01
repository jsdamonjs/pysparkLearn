import findspark
findspark.init()
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("op_flight_data") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df_1 = spark.read.option("delimiter","\t").option("header","true").csv('hdfs://localhost:9000/usr/flight_data/airport-codes-na.txt')
df_1.createOrReplaceTempView('flights')
df_1.cache()
df_2 = spark.sql(""" select * from flights where Country = 'USA' """)
df_2.write.save('hdfs://localhost:9000/usr/flight_data/tmp/1.csv')
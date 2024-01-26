import pyspark
import pandas as pd
from pyspark.sql import SparkSession
data=pd.read_csv("D:\\EDI Mapping In Python\\Learning\\ApachiSpark\\Data\\Book2.csv")

print(data)

spark= SparkSession.builder.appName("Practise").getOrCreate()
print(spark)

df_pyspark= spark.read.csv("D:\\EDI Mapping In Python\\Learning\\ApachiSpark\\Data\\Book2.csv")

print(df_pyspark)

print(type(df_pyspark))
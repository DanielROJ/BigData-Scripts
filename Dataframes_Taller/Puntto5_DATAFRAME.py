## German Daniel Rojas

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


spark = SparkSession.builder.appName('ABC').getOrCreate();


df = spark.read.csv("price_paid_records.csv", header = True);

dfOrder = df.select('Town/City','Price').groupBy('Town/City','Price').min().show();

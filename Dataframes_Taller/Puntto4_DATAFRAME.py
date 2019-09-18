## German Daniel Rojas

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


spark = SparkSession.builder.appName('ABC').getOrCreate();


df = spark.read.csv("price_paid_records.csv", header = True);

df1 = df.select('Town/City','Price', f.split('Date of Transfer','-')[0].alias('year')).where("`Town/City` == 'STAMFORD'");
df2 = df1.select('year','Price').where("year == 2015");

df3 = df2.sort('Price').show(5);



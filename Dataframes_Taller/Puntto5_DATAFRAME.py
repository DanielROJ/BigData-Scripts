## German Daniel Rojas

from pyspark.sql import SparkSession
from pyspark.sql import functions as f


spark = SparkSession.builder.appName('ABC').getOrCreate();


df = spark.read.csv("price_paid_records.csv", header = True);

df1= df.select(f.split('Date of Transfer','-')[0].alias('year'),f.split('Date of Transfer','-')[1].alias('month'));

df2 = df1.select('year','month').groupBy('year','month').count().sort(f.desc('count'));

df3 = df2.dropDuplicates(['year']).select('year','month').sort('year').show(20);



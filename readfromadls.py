import dbutils as dbutils
from pyspark.conf import SparkConf
from pyspark.sql import *

spark = SparkSession.builder \
            .config('spark.jars.packages', 'org.apache.hadoop:hadoop-azure:3.3.2')\
            .master("local[5]") \
            .getOrCreate()

spark.conf.set(
  "fs.azure.account.key.dcsaleshistory.dfs.core.windows.net",
  "v7vqUbntmfgHWDtiT+loZ8X8efFKK45R2gHW4yadrZvfGc3nILluMURaievBGoh/KioaSFQcp5A7+AStvf75Eg=="
)
datalake_raw = "abfss://raw@dcsaleshistory.dfs.core.windows.net/Sales_EAA.csv"
read_file = spark.read.csv(datalake_raw)

read_file.createOrReplaceTempView('Sales_EAA')

sql = """
      select * from Sales_EAA
      where Sales_EAA._c0 = 10
      """
df = spark.sql(sql)
#df = spark.createDataFrame(read_file)
df.show()

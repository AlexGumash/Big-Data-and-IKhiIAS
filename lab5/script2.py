from __future__ import print_function

from operator import add


from pyspark.sql import SparkSession
from pyspark import SQLContext


if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("Lab5")\
        .getOrCreate()

    sc = spark.sparkContext
    sqlContext = SQLContext(sc)

    df = sqlContext.read.csv('file:///home/bsbo228/labs/lab5/ira_users_csv_hashed.csv', header=True)
    filtered_users = df.filter(df['account_language'] != 'ru')
    # filtered_users_ids = filtered_users.select('userid')
    filtered_users.createOrReplaceTempView("users")
    filtered_users_ids = spark.sql("SELECT userid FROM users")

    tweets = sc.textFile('file:///home/bsbo228/labs/lab5/ira_tweets_csv_hashed.csv')
    tweets_header = tweets.first()
    tweets_row = tweets.filter(lambda row: row != tweets_header)
    tweets_list = tweets_row.map(lambda row: row.split(","))
    tweets_filtered = tweets_list.filter(lambda row: row[24] != '""' and row[24] != '"false"' and len(row) == 31)
    tweets_tuples = tweets_filtered.map(lambda row: (row[1].strip('"'), int(row[24].strip('"'))))
    reduced = tweets_tuples.reduceByKey(add)

    df2 = spark.createDataFrame(reduced, ['user_id', 'reply_count'])
    joined = filtered_users_ids.join(df2, filtered_users_ids['userid'] == df2['user_id'])
    joined.sort("reply_count", ascending=False).limit(1).show()

    spark.stop()
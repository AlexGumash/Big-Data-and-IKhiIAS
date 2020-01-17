from __future__ import print_function
from graphframes import *
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
    filtered_users = filtered_users.select('userid', 'user_screen_name').withColumnRenamed('userid', 'id')

    df2 = sqlContext.read.csv('file:///home/bsbo228/labs/lab5/ira_tweets_csv_hashed.csv', header=True)
    filtered_tweets = df2.filter(df2['account_language'] != 'ru')
    filtered_tweets = filtered_tweets.select('userid', 'in_reply_to_userid', 'tweetid').withColumnRenamed('in_reply_to_userid', 'dst').withColumnRenamed('userid', 'src')
    filtered_tweets = filtered_tweets.filter(filtered_tweets['dst'] != 'null')
    graph = GraphFrame(filtered_users, filtered_tweets)


    result = graph.stronglyConnectedComponents(maxIter=10)

    result.groupBy("component").count().sort("count", ascending=False).limit(10).show()

    spark.stop()


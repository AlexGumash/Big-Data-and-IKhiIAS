from __future__ import print_function

from operator import add

from pyspark.sql import SparkSession


if __name__ == "__main__":

    spark = SparkSession\
        .builder\
        .appName("Lab5")\
        .getOrCreate()

    sc = spark.sparkContext

    users = sc.textFile('file:///home/bsbo228/labs/lab5/ira_users_csv_hashed.csv')
    users_header = users.first()
    users_row = users.filter(lambda row: row != users_header)
    users_row_filtered = users_row.filter(lambda row: row.split(",")[-1] != '"ru"')
    users_row_list = users_row_filtered.map(lambda row: row.split(","))
    users_ids = users_row_list.map(lambda row: row[0])
    ids = users_ids.collect()

    tweets = sc.textFile('file:///home/bsbo228/labs/lab5/ira_tweets_csv_hashed.csv')
    tweets_header = tweets.first()
    tweets_row = tweets.filter(lambda row: row != tweets_header)
    tweets_list = tweets_row.map(lambda row: row.split(","))
    tweets_filtered = tweets_list.filter(lambda row: row[24] != '""' and row[24] != '"false"' and len(row) == 31)
    tweets_tuples = tweets_filtered.map(lambda row: (row[1], int(row[24].strip('"'))))

    reduced = tweets_tuples.reduceByKey(add)
    sort = reduced.sortBy(lambda value: value[1], ascending=False)
    filtered = sort.filter(lambda item: item[0] in ids)
    print(filtered.first())

    spark.stop()
#!/bin/bash

hdfs dfs -rm -r lab3
hdfs dfs -mkdir lab5
hdfs dfs -mkdir lab5/input

hdfs dfs -put ira_tweets_csv_hashed.csv lab5/input/
hdfs dfs -put ira_users_csv_hashed lab5/input/

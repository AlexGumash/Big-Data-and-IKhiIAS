#!/bin/bash

hdfs dfs -rm -r lab2/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/1.py,`pwd`/2.py,`pwd`/formatOutput.py \
-input lab2/input/ \
-output lab2/output/ \
-mapper `pwd`/1.py \
-combiner `pwd`/2.py \
-reducer `pwd`/2.py

hdfs dfs -cat lab2/output/part-00000

python formatOutput.py

#!/bin/bash

hdfs dfs -rm -r lab3/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/5_mapper.py,`pwd`/5_reducer.py \
-input lab3/input/ \
-output lab3/output/ \
-mapper `pwd`/5_mapper.py \
-reducer `pwd`/5_reducer.py

hdfs dfs -cat lab3/output/part-00000


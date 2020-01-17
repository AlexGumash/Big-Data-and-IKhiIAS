#!/bin/bash

hdfs dfs -rm -r lab4/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/mapper.py,`pwd`/reducer.py \
-input lab4/input/ \
-output lab4/output/ \
-mapper `pwd`/mapper.py \
-reducer `pwd`/reducer.py

hdfs dfs -cat lab4/output/part-00000



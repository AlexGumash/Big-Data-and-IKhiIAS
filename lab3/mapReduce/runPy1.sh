#!/bin/bash

hdfs dfs -rm -r lab3/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/1_mapper.py,`pwd`/1_reducer.py \
-input lab3/input/ \
-output lab3/output/ \
-mapper `pwd`/1_mapper.py \
-combiner `pwd`/1_reducer.py \
-reducer `pwd`/1_reducer.py

hdfs dfs -cat lab3/output/part-00000


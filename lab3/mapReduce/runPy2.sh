#!/bin/bash

hdfs dfs -rm -r lab3/output

yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
-D mapreduce.job.name="Cross Job via Streaming" \
-files `pwd`/2_mapper.py,`pwd`/2_reducer.py \
-input lab3/input/ \
-output lab3/output/ \
-mapper `pwd`/2_mapper.py \
-combiner `pwd`/2_reducer.py \
-reducer `pwd`/2_reducer.py

hdfs dfs -cat lab3/output/part-00000


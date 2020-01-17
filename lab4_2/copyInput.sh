#!/bin/bash

hdfs dfs -rm -r lab4
hdfs dfs -mkdir -p lab4/stage1

hdfs dfs -put data*.txt lab4/stage1/

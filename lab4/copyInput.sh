#!/bin/bash

hdfs dfs -rm -r lab4
hdfs dfs -mkdir lab4
hdfs dfs -mkdir lab4/input

hdfs dfs -put data.txt lab4/input/

#!/bin/bash

hdfs dfs -mkdir lab2
hdfs dfs -mkdir lab2/input

hdfs dfs -put orders.txt lab2/input/

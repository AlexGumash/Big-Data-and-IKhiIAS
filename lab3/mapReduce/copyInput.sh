#!/bin/bash

hdfs dfs -rm -r lab3
hdfs dfs -mkdir lab3
hdfs dfs -mkdir lab3/input

hdfs dfs -put data_teams.txt lab3/input/
hdfs dfs -put data_cars.txt lab3/input/
hdfs dfs -put data_teammembers.txt lab3/input/

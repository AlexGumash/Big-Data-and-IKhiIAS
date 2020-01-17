#!/bin/bash

script () {
    stages=$1
    yarn jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-*.jar \
    -D mapreduce.job.name="HITS algorithm Job via Streaming" \
    -files `pwd`/mapper.py,`pwd`/reducer.py \
    -input "lab4/stage$stages/" \
    -output "lab4/stage$((stages+1))"/ \
    -mapper `pwd`/mapper.py \
    -reducer `pwd`/reducer.py
}


./copyInput.sh
ITERATIONS=$1
for ((i=1; i <= ${ITERATIONS}; i++)); do
    script ${i}
done


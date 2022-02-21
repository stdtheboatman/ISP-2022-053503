#!/bin/bash

name=""
if [ $# -ne 0 ]
    then
        name="--name $1"
fi

args=""
if [ $# -gt 1 ]
    then
        args=$2
fi

echo ${args}

mkdir -p data

docker run ${name} \
${args} \
--mount type=bind,src="${PWD}/data",target="/app/data" \
theboatman/first-lab
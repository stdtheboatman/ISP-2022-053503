#!/bin/bash

name=""
if [ $# -ne 0 ]
    then
        name="--name $1"
fi
        
echo ${args}

docker run ${name} \
${args} \
--mount type=bind,src="${PWD}/data",target="/app/data" \
theboatman/first-lab
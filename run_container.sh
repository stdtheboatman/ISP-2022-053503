#!/bin/bash

name=$1
args=$2

echo ${args}

docker run --name ${name} \
${args} \
--mount type=bind,src="${PWD}/local",target="/app/data" \
theboatman/first-lab
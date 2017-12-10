#!/usr/bin/env bash


for a in "$@"
do
command+="$a "
done

curl -X POST http://localhost:80 -d "$command"
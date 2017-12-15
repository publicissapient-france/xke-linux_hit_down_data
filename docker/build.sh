#!/usr/bin/env sh

docker rmi linuxhitdowndata/first
docker build -t 'linuxhitdowndata/first' .

#!/usr/bin/env sh

docker rmi discovery:latest
docker build -t 'discovery' .

#!/usr/bin/env sh

docker rmi hit_down_data:latest
docker build -t 'hit_down_data' .

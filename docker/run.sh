#!/usr/bin/env sh

docker run \
    --name hit_down_data \
    --hostname discover.local \
    --privileged=true \
    -i -t --rm\
    hit_down_data \
    /bin/bash



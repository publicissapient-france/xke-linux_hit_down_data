#!/usr/bin/env sh

docker run \
    --name discovery \
    --hostname discover.local \
    --privileged=true \
    -i -t --rm\
    --user=newuser\
    discovery \
    /bin/bash



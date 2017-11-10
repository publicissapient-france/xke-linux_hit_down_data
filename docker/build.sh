#!/usr/bin/env sh

docker rmi dude/discovery
docker build -t 'discovery' .

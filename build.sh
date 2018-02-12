#!/usr/bin/env sh

docker rmi linuxhitdowndata/first
echo "build..."
docker build -t 'linuxhitdowndata/first' -f docker/Dockerfile .  1>/dev/null

BUILD_RETURN_CODE=$?

echo "Now execute ./run.sh"


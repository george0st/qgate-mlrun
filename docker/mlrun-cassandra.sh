#!/bin/sh

docker pull cassandra:5.0-rc1
docker run --name mlrun-cassandra -p 9042:9042 -d cassandra:5.0-rc1

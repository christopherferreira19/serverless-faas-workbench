#! /bin/bash

DOCKER=${DOCKER:-docker}
MINIO=minio/minio:11563-d95ceb3

$DOCKER pull ${MINIO}
$DOCKER run -p 9000:9000 ${MINIO} server /data
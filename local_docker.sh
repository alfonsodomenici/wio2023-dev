#!/bin/sh
docker build -t wio2023 .
docker rm -f wio2023 || true && docker run -d -p 5000:5000 \
    --network  db \
    --env-file ./.env.docker.local \
    --name wio2023 wio2023 
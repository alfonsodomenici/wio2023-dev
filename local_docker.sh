#!/bin/sh
docker build -t dhtssdev/wio2023 .
docker rm -f wio2023 || true && docker run -d -p 5000:5000 --name wio2023 dhtssdev/wio2023 
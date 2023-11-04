FROM python:3.9-slim-bullseye

ENV FLASK_APP run.py
ENV FLASK_CONFIG production

RUN adduser --disabled-password --disabled-login --shell=/bin/bash --gecos '' wio
USER wio

WORKDIR /home/wio

COPY requirements.txt ./
RUN python -m venv venv
RUN venv/bin/pip install -r requirements.txt

COPY src src
#COPY migrations migrations
COPY run.py boot.sh ./

# run-time configuration
EXPOSE 5000
ENTRYPOINT ["/bin/bash", "./boot.sh"]


# FROM ubuntu

# RUN apt-get update && \
#  apt-get upgrade -y && \
#  apt-get install python3-pip curl -y &&\
#  pip3 install pipenv

# RUN pip3 install pandas numpy


FROM ubuntu

ENV PYTHONBUFFER = 1

RUN apt update && \
    apt upgrade -y && \
    apt install python3 python3-pip curl -y && \
    pip3 install pandas numpy

# I have no idea how to make this work

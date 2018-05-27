FROM ubuntu:16.04
MAINTAINER Mevin Babu "mevin.chirayath@galepartners.com"

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get install -y git python2.7 python-pip python-dev postgresql-server-dev-all
ADD requirements.txt /srv/requirements.txt
ADD requirements-dev.txt /srv/requirements-dev.txt
WORKDIR /srv/
RUN pip install -U pip
RUN pip install -r /srv/requirements.txt
RUN rm -rf /usr/local/lib/python2.7/dist-packages/requests
RUN pip install -r /srv/requirements-dev.txt


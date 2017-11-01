FROM python:3.6

LABEL maintainer "uehara1414 <akiya.noface@gmail.com>"

RUN apt-get update
RUN apt-get install -y openssl mecab libmecab-dev mecab-ipadic-utf8 python-mecab
RUN mkdir -p /usr/lib/mecab/dic
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git /tmp/neologd
RUN /tmp/neologd/bin/install-mecab-ipadic-neologd -n -y
RUN rm -rf /tmp/neologd
RUN pip install mecab-python3

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN pip install -r requirements.txt

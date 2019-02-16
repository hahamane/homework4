FROM ubuntu:16.04
MAINTAINER Dae Hun Park
RUN mkdir -p /home/work/
RUN apt-get update
RUN apt-get install -y python3-pip
RUN pip3 install numpy pandas
ADD ./* /home/work/
ENTRYPOINT python3 /home/work/parcer.py

FROM centos:latest

#Installation JQ
RUN yum install -y epel-release && yum install -y jq && yum install -y python34

#COPY daemon
ADD /deamon/ /root/
RUN chmod 700  /root/* && chmod 700 /usr/bin/python*

#password compte root
RUN echo 'chocolat' |passwd root --stdin

#nouvel utilisateur
RUN useradd -ms /bin/bash newuser
USER newuser
WORKDIR /home/newuser

#COPY data
ADD /logs/ /home/newuser/log/
ADD /csv/ /home/newuser/csv/
ADD /json/ /home/newuser/json/
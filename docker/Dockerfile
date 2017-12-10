
FROM centos:latest

#Installation JQ
RUN yum install -y epel-release && yum install -y jq && yum install -y python34

#COPY daemon
ADD /deamon/ /root/
RUN chmod 700  /root/* && chmod 700 /usr/bin/python*

#password compte root
RUN echo 'chocolat' | passwd root --stdin

#COPY cmd
ADD /shell/send.sh /opt/shell/send.sh
ADD /shell/start.sh /opt/shell/start.sh
ADD /shell/start.sh /opt/shell/halt.sh


RUN chmod 777 /opt/shell/send.sh && chmod 700 /opt/shell/start.sh && chmod 777 /opt/shell/halt.sh && ln -s /opt/shell/halt.sh /usr/sbin/halt


#utilisateur luc
RUN useradd -ms /bin/bash luc


#utilisateur andre
RUN useradd -ms /bin/bash andre
WORKDIR /home/andre
RUN echo "alias send='/opt/shell/send.sh'" >> /home/andre/.bashrc && echo "send hello" >> /home/andre/.bash_history

#COPY data
RUN chmod 777 /var/log/* && chmod 777 /home/*
ADD /var.log/ /var/log/

ADD /csv/ /home/csv/
ADD /json/ /home/json/
ADD /doc/README.md /home/andre/README.md

# start Deamon
ENTRYPOINT  /opt/shell/start.sh && su andre && /bin/bash


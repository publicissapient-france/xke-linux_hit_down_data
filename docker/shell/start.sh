#!/usr/bin/env bash

cd /root
nohup python3 serveur.py >> /root/logs/daemon.txt 2>&1 &
cd /home/andre
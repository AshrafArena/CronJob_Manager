# CronJob Manager

A Flask web application to manage CronJobs through a UI instead of an editor.

# Features

- List existing cron jobs
- Add new cron jobs
- Delete cron jobs

# Installation:

## Switch to root user
sudo su -

## Update system and install required packages
yum update -y

yum install -y python3 python3-pip cronie git

## Start and enable crond service
systemctl start crond

systemctl enable crond

## Clone the GitHub repository
git clone https://github.com/AshrafArena/CronJob_Manager.git

cd CronJob_Manager

## Install Python dependencies
pip3 install -r requirements.txt

## Run the Flask application
sudo python3 run.py

NOTE: The server is listening on port 80, browsers default to 443 (https), so just remove the "s" from 
your VM's public IP and you will be able to access the app.


    

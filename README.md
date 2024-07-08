# CronJob Manager

A self-developed Flask web application to manage user-based CronJobs on linux-based systems.

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

## Switch to ec2-user home directory
cd /home/ec2-user

## Clone the GitHub repository
git clone https://github.com/AshrafArena/CronJob_Manager.git

cd CronJob_Manager

## Install Python dependencies
pip3 install -r requirements.txt

## Run the Flask application
sudo python3 run.py



## Tree Structure

Your directory structure for the app should look very similiar to this:


![Dir Tree](https://github.com/AshrafArena/CronJob_Manager/assets/129840697/fa0f90c0-521a-45cb-883e-8937777d9f98)

    

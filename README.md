# Cron Job Manager

A Flask web application to manage user-based cron jobs.

## Features

- List existing cron jobs
- Add new cron jobs
- Delete cron jobs

## Installation

# Switch to root user
sudo su -

# Update system and install required packages
yum update -y

yum install -y python3 python3-pip cronie git

# Start and enable crond service
systemctl start crond
systemctl enable crond

# Switch to ec2-user home directory
cd /home/ec2-user

# Clone the GitHub repository
git clone https://github.com/AshrafArena/CronJob_Manager.git

cd CronJob_Manager

# Install Python dependencies
pip3 install -r requirements.txt

# Run the Flask application
sudo python3 run.py



## Tree structure

Your directory structure for the app should look very similiar to this:

cronjob_manager/
├── README.md
├── app
│   ├── 1
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-39.pyc
│   │   ├── crontab_manager.cpython-39.pyc
│   │   └── routes.cpython-39.pyc
│   ├── crontab_manager.py
│   └── routes.py
├── requirements.txt
├── run.py
└── templates
    └── index.html

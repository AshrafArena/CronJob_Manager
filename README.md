# Cron Job Manager

A Flask web application to manage user-based cron jobs.

## Features

- List existing cron jobs
- Add new cron jobs
- Delete cron jobs

## Installation

1. Switch to root user
sudo su -

2. Update system and install required packages
yum update -y
yum install -y python3 python3-pip cronie git

3. Start and enable crond service
systemctl start crond
systemctl enable crond

4. Switch to ec2-user home directory
cd /home/ec2-user

5. Clone the GitHub repository
git clone https://github.com/AshrafArena/CronJob_Manager.git
cd CronJob_Manager

6.Install Python dependencies
pip3 install -r requirements.txt

7. Run the Flask application
python3 run.py


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

from flask import render_template, request, jsonify
from app import app
from app.crontab_manager import list_cron_jobs, add_cron_job, delete_cron_job

@app.route('/')
def index():
    jobs = list_cron_jobs()
    return render_template('index.html', jobs=jobs)

@app.route('/add_cronjob', methods=['POST'])
def add_cronjob():
    data = request.get_json()
    cron_expression = data['cron_expression']
    command = data['command']
    
    # Debugging: Print the received data
    print(f"Received cron_expression: {cron_expression}")
    print(f"Received command: {command}")
    
    # Validate cron expression format (basic validation)
    cron_parts = cron_expression.split()
    if len(cron_parts) != 5:
        return jsonify({'status': 'error', 'message': 'Invalid cron expression format'}), 400
    
    success, message = add_cron_job(cron_expression, command)
    if success:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': message}), 500

@app.route('/delete_cronjob/<int:index>', methods=['DELETE'])
def delete_cronjob(index):
    success, message = delete_cron_job(index)
    if success:
        return jsonify({'status': 'success'})
    else:
        return jsonify({'status': 'error', 'message': message}), 500


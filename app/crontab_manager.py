import subprocess

def list_cron_jobs():
    result = subprocess.run(['crontab', '-l'], capture_output=True, text=True)
    if result.returncode != 0:
        return []
    return result.stdout.strip().split('\n')

def add_cron_job(cron_expression, command):
    cron_job = f"{cron_expression} {command}"
    existing_jobs = list_cron_jobs()
    new_cron_content = '\n'.join(existing_jobs + [cron_job])
    process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(new_cron_content + '\n')
    
    if process.returncode != 0:
        print(f"Error adding cron job: {stderr}")
        return False, stderr
    return True, stdout

def delete_cron_job(index):
    existing_jobs = list_cron_jobs()
    if index < len(existing_jobs):
        existing_jobs.pop(index)
        new_cron_content = '\n'.join(existing_jobs)
        process = subprocess.Popen(['crontab', '-'], stdin=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate(new_cron_content + '\n')
        
        if process.returncode != 0:
            print(f"Error deleting cron job: {stderr}")
            return False, stderr
        return True, stdout
    return False, "Index out of range"


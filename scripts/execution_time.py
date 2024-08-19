import time
import subprocess

def playbook_execution_time(playbook_path):
    start_time = time.time()

    # Execute the playbook
    subprocess.run(['ansible-playbook', playbook_path])

    end_time = time.time()
    execution_time = end_time - start_time

    print(f"Time to Execute Playbook: {execution_time} seconds")
    return execution_time

if __name__ == "__main__":
    execution_time = playbook_execution_time('../config/ansible/playbooks/bandwidth_adjudtment.yaml')
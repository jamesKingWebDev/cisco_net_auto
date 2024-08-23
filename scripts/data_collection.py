import paramiko
import os

def collect_data(host, username, password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username, password)

    stdin, stdout, stderr = client.exec_command('show interfaces')
    data = stdout.read().decode()
    client.close()

    # Storing generated data to a file
    with open('data/interfaces.txt', 'w') as f:
        f.write(data)

if __name__ == "__main__":
    collect_data('sandbox-iosxe-latest-1.cisco.com', 'developer', 'C1sco12345')

import paramiko

def execute_command(host, username, password, command):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, username=developer, password=C1sco12345)

    stdin, stdout, stderr = client.exec_command(command)
    output = stdout.read().decode()
    client.close()
    return output

if __name__ == "__main__":
    output = execute_command('sandbox-iosxe-latest-1.cisco.com', 'developer', 'C1sco12345', 'reveal route of the ip')
    print(output)

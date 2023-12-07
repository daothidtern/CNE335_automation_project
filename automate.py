#Daothi tern
#Automate ssh

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Use double backslashes or a raw string for the file path

ssh.connect(hostname='34.209.241.162', username='ubuntu', key_filename=r'C:\Users\thidd\PycharmProjects_automation\keypair.pem')


# Run update command
update_command = 'sudo apt-get update'
stdin, stdout, stderr = ssh.exec_command(update_command)

# Print the output of the update command
print("Update Command Output:")
for line in stdout.read().decode().splitlines():
    print(line)

# Run upgrade command
upgrade_command = 'sudo apt-get upgrade -y'
stdin, stdout, stderr = ssh.exec_command(upgrade_command)

# Print the output of the upgrade command
for line in stdout.read().splitlines():
    print(line)

# Disconnect from the server
ssh.close()
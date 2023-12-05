#Daothi tern
#Automate ssh
import paramiko

import paramiko
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Use double backslashes or a raw string for the file path
ssh.connect(hostname='18.246.215.35', username='ubuntu', key_filename=r'C:\Users\thidd\PycharmProjects_automation\your_private_key.pem')



# Run update command
update_command = 'sudo apt-get update'
stdin, stdout, stderr = ssh.exec_command(update_command)

# Print the output of the update command
print("Update Command Output:")
for line in stdout.read().splitlines():
    print(line)

# Run upgrade command
upgrade_command = 'sudo apt-get upgrade -y'
stdin, stdout, stderr = ssh.exec_command(upgrade_command)

# Print the output of the upgrade command
print("\nUpgrade Command Output:")
for line in stdout.read().splitlines():
    print(line)

# Disconnect from the server
ssh.close()
import os
import subprocess
os.system("ping -n 18.246.215.35 ")

class Server:
    """ Server class for representing and manipulating servers. """

    def __init__(self, server_ip):
        # TODO -
        self.server_ip = server_ip
        self.ping()

    def ping(self):
        # TODO - Use os module to ping the server
        try:
            # Use subprocess to run the ping command
            result = subprocess.run(["ping", "-n", "4", self.server_ip], capture_output=True, text=True, check=True)

            # Check if the ping was successful
            if "0% packet loss" in result.stdout:
                return True
            else:
                return False

        except subprocess.CalledProcessError:
            # An error occurred (e.g., invalid IP address, network unreachable)
            return False


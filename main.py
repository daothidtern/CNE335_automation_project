# This is the template code for the CNE335 Final Project
# Daothidtern
# CNE 335 Fall
import server
def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by daothid")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
    ec2_server_ip ="18.246.215.35"
    ec2_server = server.Server(ec2_server_ip)

    if ec2_server.ping():
        print(f"The server at {ec2_server_ip} is reachable.")
    else:
        print(f"The server at {ec2_server_ip} is not reachable.")
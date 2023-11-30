# This is the template code for the CNE335 Final Project
# Justin Ellis
# CNE 335 Fall

def print_program_info():
    # TODO - Change your name
    print("Server Automator v0.1 by Your Name")

# This is the entry point to our program
if __name__ == '__main__':
    print_program_info()
    # TODO - Create a Server object
    # TODO - Call Ping method and print the results
    server_ip = "18.246.215.35"
    my_server = Server(server_ip)
    if my_server.ping():
        print(f"The server at {server_ip} is reachable.")
    else:
        print(f"The server at {server_ip} is not reachable.")
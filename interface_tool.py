import argparse
from turtle import clear
from paramiko import SSHClient


def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="-i or --interface to specify interface")   
    interface = parser.parse_args().interface
    if not interface:
        print("\nEnter an interface / '-help' for help\n")
        exit()
    return str(interface)

def printMenu():
    print("\n\n================================================\n")
    print("  Welcome to interface tool, choose an option: \n")
    print("================================================\n")
    print("1. ifconfig\n2. Do stuff\n3. Do stuff\n\n Type 'q' to quit")
    in_1 = input(">")
    return in_1

def manageMenu(client, first_input):
    input = first_input
    while True:
        if input == 'q':
            break
        if input == '1':
            executeCommand(client)
        else:
            print("[-] Invalid input.")
        input = printMenu()
    

def SSHConnect():
    #ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("ifconfig eth0")
    #print(f'STDOUT: {ssh_stdout.read().decode("utf8")}')
    client = SSHClient()
    client.load_system_host_keys()
    host = input("> Enter hostname: ")
    user = input("> Enter username: ")
    key = input("> Enter key path: ")
    print("[+] Establishing connection...")
    client.connect(hostname=host, username=user, key_filename=key, timeout=5)
    return client

def trySSHConnect():
    try:
        client = SSHConnect()
    except TimeoutError:
        print("[-] Failed to establish connection.")
        exit()
    print("[+] Connected.")
    return client

def executeCommand(client):
    stdin = client.exec_command("ifconfig eth0")
    print(f'STDOUT: {stdin[1].read().decode("utf8")}')


# ============================ MAIN FUNCTION =================================== #
def __main__():
    #iface = getArgs()
    client = trySSHConnect()

    input = printMenu()
    manageMenu(client, input)

    print("[+] Closing interface tool, terminating connection...")
    try:
        client.close()
        print("[+] Done.")
    except:
        print("[-] Client could not be closed.")

__main__()




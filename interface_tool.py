import argparse
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
    print("================================================\n\n")
    print("1. Connect\n2. Do stuff\n3. Do stuff")
    in_1 = input(">")
    return in_1

def SSHConnect():
    #ssh_stdin, ssh_stdout, ssh_stderr = client.exec_command("ifconfig eth0")
    #print(f'STDOUT: {ssh_stdout.read().decode("utf8")}')
    client = SSHClient()
    client.load_system_host_keys()
    print("[+] Establishing connection...")
    client.connect(hostname="20.68.195.79", username="cemg", key_filename='C:\\Users\\cemg\\Documents\\VM-cemg_key.pem')
    return client

def executeCommand(client):
    stdin = client.exec_command("ifconfig lo")
    print(f'STDOUT: {stdin[1].read().decode("utf8")}')


# ============================ MAIN FUNCTION =================================== #
def __main__():
    iface = getArgs()
    client = SSHConnect()
    input = printMenu()
    if input == '1':
        executeCommand(client)
    client.close()
__main__()




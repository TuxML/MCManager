#!/usr/bin/python2

import paramiko
import os
import getpass
from multiprocessing import Pool
from sys import argv
from contextlib import closing


def makeSSHClient(number):
    listClient = [paramiko.SSHClient() for _ in range(number)]
    for client in listClient:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pass
    return listClient
    pass


def line_buffered(f):
    line_buf = ""
    while not f.channel.exit_status_ready():
        line_buf += f.read(1)
        if line_buf.endswith('\n'):
            yield line_buf
            line_buf = ''


def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1


def clientConnect(client, clientName, username, password):
    print("Debut de la connexion")
    print("{}".format(idPC))
    client.connect('{}.istic.univ-rennes1.fr'.format(clientName), username =  username, password = password)
    stdin, stdout, stderr = client.exec_command('cd /private/student/6/46/14002346/Documents/ProjetIrma; ./MLfood.py 1')
    client.close()
    pass


if __name__ == '__main__':
    listOrdi = open('BaseDeData.txt', 'r')
    listClient = makeSSHClient(file_len("BaseDeData.txt"))
    username = raw_input("Username:")
    password = getpass.getpass("Password:")
    for client in listClient:
        clientName = listOrdi.readLines()
        try:
            pid = os.fork()
        except OSError:
            sys.stderr.write("Could not create the child process")
            continue
        if pid == 0:
            clientConnect(client, clientName, username, password)
            exit()
            pass
        else:
            print("In the parent process after forking children number {}".format(idPC))
        idPC += 1
        pass
    print("End of the forking")
    for endClient in listClient:
        finished = os.waitpid(0, 0)
        print(finished)
        pass

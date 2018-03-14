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


def clientConnect(listClient, idPC):
    username = input("Username:")
    password = raw_input("Password:")
    for client in listClient:
        print("Debut de la connexion")
        print("{}".format(idPC))
        client.connect('e212m0{}.istic.univ-rennes1.fr'.format(idPC), username =  username, password = password)
        stdin, stdout, stderr = client.exec_command('cd /private/student/6/46/14002346/Documents/ProjetIrma; ./MLfood.py 1')
        client.close()
        pass
    pass


if __name__ == '__main__':
    forks = 2
    idPC = 1
    listClient = makeSSHClient(int(argv[1]))
    for idFork in range(forks):
        try:
            pid = os.fork()
        except OSError:
            sys.stderr.write("Could not create the child process")
            continue
        if pid == 0:
            clientConnect(listClient, idPC)
            pass
        else:
            print("In the parent process after forking children number {}".format(idFork))
        idPC += 1
        pass
    print("End of the forking")
    for i in range(forks):
        finished = os.waitpid(0, 0)
        print(finished)
        pass

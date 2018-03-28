#!/usr/bin/python2.7

import paramiko
import os
import getpass

import sys


def makeSSHClient(number):
    listClient = [paramiko.SSHClient() for _ in range(number)]
    print(listClient)
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
    Log_host = open('{}.log'.format(clientName), 'w')
    print("Debut ssh")
    print(clientName)
    client.connect("{}.istic.univ-rennes1.fr".format(clientName), username =  username, password = password)
    print("connexion reussi, debut MLFood")
    stdin, stdout, stderr = client.exec_command('cd /private/student/6/46/14002346/Documents/ProjetIrma; ./MLfood.py 1 --dev')
    for line in stdout:
        Log_host.write(line)
    client.close()
    print("End ssh")
    pass


if __name__ == '__main__':
    listOrdi = open('BaseDeDataTest.txt', 'r')
    number_ordi = 0
    for line in listOrdi:
        number_ordi += 1
    listOrdi.seek(0)
    print(number_ordi)
    listClient = makeSSHClient(number_ordi)
    username = raw_input("Username:")
    password = getpass.getpass("Password:")
    for client in listClient:
        clientName = listOrdi.readline()
        clientName = clientName.strip('\n')
        try:
            pid = os.fork()
        except OSError:
            sys.stderr.write("Could not create the child process")
            continue
        if pid == 0:
            clientConnect(client, clientName, username, password)
            exit()
            pass
        pass
    for endClient in listClient:
        finished = os.waitpid(0, 0)
        pass

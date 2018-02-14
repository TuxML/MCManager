#!/usr/bin/python2

import paramiko
from sys import argv


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


def clientConnect(listClient):
    i = 1
    for client in listClient:
        print("Debut de la connexion")
        print("{}".format(i))
        client.connect('e212m0{}.istic.univ-rennes1.fr'.format(i), username = '14002346', password='Vivelavie2*')
        stdin, stdout, stderr = client.exec_command('cd /private/student/6/46/14002346/Documents/ProjetIrma; ./MLfood.py 10')
        for ligne in line_buffered(stdout):
            print(ligne)
            pass
        i += 1
        client.close()
        pass
    pass


if __name__ == '__main__':
    listClient = makeSSHClient(int(argv[1]))
    clientConnect(listClient)

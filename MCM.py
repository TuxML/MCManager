#!/usr/bin/python2

import paramiko


def makeSSHClient(number):
    listClient = [paramiko.SSHClient() for _ in range(number)]
    for client in listClient:
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        pass
    return listClient
    pass


def clientConnect(listClient):
    i = 1
    for client in listClient:
        print("Debut de la connexion")
        client.connect('e008m0{}.istic.univ-rennes1.fr'.format(i), username = '14002346', password='Vivelavie2*')
        stdin, stdout, stderr = client.exec_command('cd Documents/ProjetIrma')
        print(stdin + stdout + stderr)
        stdinML, stdoutML, stderrML = client.exec_command('./MLFood.py 10')
        print(stdinML + stdoutML + stderrML)
        i += 1
        client.close()
        pass
    pass


if __name__ == '__main__':
    listClient = makeSSHClient(5)
    clientConnect(listClient)

#!/usr/bin/python3


import pssh.pssh_client as pssh
import subprocess
import os
import getpass


def connect():
    passwd = getpass.getpass()

    client = pssh.ParallelSSHClient("127.0.0.1", user="alemasle" , password=passwd)
    client.run_command('uname')
    output = client.get_last_output()
    for host, host_output in output.items():
        for line in host.stdout:
            print(line)
    client.close()


def hostlist():
    #Ask for machines adress list ( file if possible )
    pass

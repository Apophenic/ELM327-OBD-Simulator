import IO
import sys
import os
import subprocess
from socket import socket

__workingdir = os.path.dirname(os.path.abspath(__file__))

def startserver(address, port, startshell):
    """Starts a simulator instance at the given address and port.
    If startshell is True, a seperate python instance will be created
    that is connected to the server"""
    s = socket()
    s.bind((address, port))
    s.listen(2)

    if startshell:
        subprocess.Popen([sys.executable, __workingdir + '\Shell.py', address, str(port)])

    c, addr = s.accept()

    while True:
        try:
            data = c.recv(16).decode('utf-8')
            data = str.replace(data, '\r', '')  # ELM Queries terminate w/ carriage return. Remove.
        except:
            print('ERROR: Failed to parse byte string')
            continue

        response = IO.readinputbytes(data)

        c.send(str.encode(response.getresponse()))

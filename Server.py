import IO
import sys
import subprocess
from socket import socket

def startserver(address, port, startshell):
    """Starts a simulator instance at the given address and port.
    If startshell is True, a seperate python instance will be created
    that is connected to the server"""
    s = socket()
    s.bind((address, port))
    s.listen(1)

    if startshell:
        subprocess.Popen([sys.executable, 'Shell.py', address, str(port)])

    c, addr = s.accept()

    while True:
        try:
            data = c.recv(8).decode('utf-8')
        except:
            print('ERROR: Failed to parse byte string')
            continue

        response = IO.readinputbytes(data)

        if response is None:
            c.send(str.encode('ERROR'))
        else:
            c.send(str.encode(response.getresponse()))

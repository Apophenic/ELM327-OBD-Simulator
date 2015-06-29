import sys
import os
from socket import socket

# These args come from Server's subprocess.Popen()
address = sys.argv[1]
port = int(sys.argv[2])

s = socket()
s.connect((address, port))

while True:
    query = input("Send: ")
    if query == 'exit':
        os.system('taskkill /f /im python.exe')  # exit server + shell (does this work outside windows?)
    else:
        s.send(str.encode(query.upper()))
        print(s.recv(512).decode('utf-8'))

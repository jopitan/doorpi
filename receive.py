#!/usr/bin/python

import socket
import struct
from time import sleep
import os
import subprocess as sp
import atexit

multicast_addr = '224.0.0.1'
bind_addr = '0.0.0.0'
port = 3000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
membership = socket.inet_aton(multicast_addr) + socket.inet_aton(bind_addr)

sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, membership)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

sock.setblocking(0)

sock.bind((bind_addr, port))

def exitTerminal():
        sp.Popen(['python', '/var/www/html/close_door.py'])

atexit.register(exitTerminal)

extProc = None

while True:
        try:
                msg = sock.recv(1024)
                if(extProc == None):
                        extProc = sp.Popen(['python', '/var/www/html/door.py', '5'])
                status = sp.Popen.poll(extProc)
                if(status == 0):
                        extProc = None
        except socket.error, e:
                continue

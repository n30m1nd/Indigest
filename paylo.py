# -*- coding: UTF-8 -*-

__author__ = 'n30m1nd'

### THIS FILE HAS NO SENSE NOW ###

import hashlib
import socket
import time

password="admin"
realm="raramasa"
nonce="00000defCA5300004fbd9"

uri="/"
method="GET"

num_sess = raw_input("Last session: ")
num_sess = int(num_sess)

fd = open("digest10k.txt")
lines = fd.readlines()
fd.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.200", 1234))
s.send("GET / HTTP/1.1\n")
rec = s.recv(1024)
print rec
s.close()

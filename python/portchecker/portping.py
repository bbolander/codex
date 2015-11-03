#!/usr/bin/python
#
#   portcheck.py
#
#   Brian Bolander
#
#   

import socket
import sys

def usage():
    print "portping usage: portping <hostname> <port>\n"

    

port = int(sys.argv[2])
host = sys.argv[1]

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.connect((host, port))
except socket.gaierror, e:
    print "gaierror: error connecting to server: %s" % e
    #sys.exit(1)
except socket.error, e:
    print "error: %s" % e[1]
except socket.timeout, e:
    print "timeout: %s" % e[1]
else:
   print "Connected to port %d" % port

s.close


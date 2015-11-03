#!/usr/bin/python
#
#   portchecker.py
#
#   Brian Bolander
#
#   

import socket
import sys
import re
import pdb
import getopt
import os

"""
_______________________________________________________________________________

   readportsfile
_______________________________________________________________________________

"""

def readportsfile(filename):
   """
   Read the file that contains the information about the ports and return
   a data structure with the following format.

   ports = {

   #   hostname        port name      port
   
       'codex':       {
                       'telnet':       22,
                       'webserver':    80 
                  },

       'etmessrv01':    {
                       'asadmin':      4848,
                       'webserver':    80 
                  },
   }

   File format: One port per line...

   <hostname> <port name (one word, non-whitespace characters)> <port number>
   <hostname> <port name (one word, non-whitespace characters)> <port number>
   .
   .
   .

   filename:   The name of the file to be read.
   """
   debug = False

   ports = dict()

   hostname =       ""
   portnumber =   ""
   portname =      ""

   #pdb.set_trace()

   try:
      portsfile = open(portscpath + filename, 'r')
   except IOError:
      try:
         portsfile = open(filename, 'r')
      except IOError, e:
         print "Error opening file: %s" % e
         sys.exit(2)

   for line in portsfile:
      line = line.rstrip("\n")
      #print line
      #if re.match('^[^#]\w*\W*\w*\W*\d*$', line) and line:
      if re.match('^[^#]\S*\W*\w*\W*\d*$', line) and line:
         hostname, portname, portnumber = line.split()
         if debug:
            print
            print "Host:\t%s" % hostname
            print "Descr:\t%s" % portname
            print "Port:\t%s" % portnumber
         if ports.has_key(hostname):
            ports[hostname][portname] = int(portnumber)
         else:
            ports[hostname] = {portname: int(portnumber)}
      else:
         if re.match('^[^#].*$', line) and line:
            print "Format check failed for line:"
            print line

   return(ports)


"""
_______________________________________________________________________________

   portping
_______________________________________________________________________________

"""


def portping(hostname, port):
   """
   Ping a port and return the result in status string.

   hostname:    The hostname of the machine.
   port:      The port number.
   """

   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   s.settimeout(5)

   status = "success"
   
   try:
       s.connect((hostname, port))
   except socket.gaierror, e:
       status = "gaierror: %s" % e[1]
   except socket.error, e:
       status = "error: %s" % e[0]
   except socket.timeout, e:
       status = "timeout: %s" % e[1]
   except:
      status = "portping: Unknown error."

   s.close()

   return(status)

"""
_______________________________________________________________________________

   usage
_______________________________________________________________________________

"""

def usage():
   print "portchecker -c <configuration file> [-f]"

   print "   %-24s" % "-c <config file>",
   print "Name of the configuration file located in /usr/share/portchecker/conf"

   print "   %-24s" % "-f", 
   print "Firewall check; only throw an error if there is a timeout."

   print "   %-24s" % "-l", 
   print "List the configuration files located in /usr/share/portchecker/conf."
"""
_______________________________________________________________________________

   printport
_______________________________________________________________________________

"""

def printport(hostname, portname):
   print "%-24s" % hostname,
   print "%-24s" % portname,
   print "%-6d" % ports[hostname][portname],
   print "\t",
   print "%s" % status

"""
_______________________________________________________________________________

   listconfigs
_______________________________________________________________________________

"""

def listconfigs():
   print "Config files located in %s:" % portscpath
   filenames = os.listdir(portscpath)
   for filename in filenames:
      print "\t%s" % filename


"""
_______________________________________________________________________________

   Main
_______________________________________________________________________________

"""

try:
   opts, args = getopt.getopt(sys.argv[1:], "c:fl")
except getopt.GetoptError, err:   
   print str(err)
   usage()
   sys.exit(2)

portscpath  = "/usr/share/portchecker/"
portsfile   = "ports.txt"
mode        = "NORMAL"

for opt, arg in opts:
   if opt == "-c":
      portsfile = arg
   elif opt == "-f":
      mode = "FW_CHECK"
   elif opt == "-l":
      listconfigs()
      sys.exit()

ports = readportsfile(portsfile)

for hostname in ports:
   for portname in ports[hostname]:
      status = portping(hostname, ports[hostname][portname])
      if mode == "NORMAL":
         printport(hostname, portname)
      elif mode == "FW_CHECK" and re.match('^.*timed out.*$', status) :
         printport(hostname, portname)


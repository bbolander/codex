#!/usr/bin/python
#
#   process_respawn.py
#
#   Brian Bolander
#
#

import sys
import os
from time import time, sleep

def allow_respawn(process_name, intervals):

   # Holds respawn time current_time - respawn time
   respawn_intervals = []
   # Current time in seconds since the epoch.
   current_time = int(time())

   # Record this respawn request time.
   # Creates the file for this proc if it DNE.
   proc_respawns_file = open(process_name, "a")
   proc_respawns_file.write(str(current_time) + "\n")
   proc_respawns_file.close()

   # Read respawn time file
   proc_respawns_file = open(process_name, "r")
   
   for line in proc_respawns_file:
      # Calculate the respawn interval for each respawn
      respawn_intervals.append(current_time - int(line))

   # Check the intervals
   # Some indexes for clarity.
   interval_time = 0
   allowed_respawns = 1
   for interval in intervals:
      # Number of respawns for this interval
      no_respawns = 0
      for respawn_interval in respawn_intervals:
         if respawn_interval <= interval[interval_time]:
            no_respawns += 1
      
      print "Interval: 0 - %s Allowed respawns: %s Number of respawns: %s" % (str(interval[interval_time]), \
                                                                              str(interval[allowed_respawns]), \
                                                                              no_respawns)
      if no_respawns > interval[allowed_respawns]:
         return(False)

   return(True)

###############################################################################
#
# main
#
###############################################################################


for i in range(4):
   print "Allow respawn: %s" % allow_respawn("procname", [[5, 5], [20, 10]])

sleep(6)

for i in range(4):
   print "Allow respawn: %s" % allow_respawn("procname", [[5, 5], [20, 10]])

sleep(6)

for i in range(4):
   print "Allow respawn: %s" % allow_respawn("procname", [[5, 5], [20, 10]])

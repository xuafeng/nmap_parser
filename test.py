#!/usr/bin/python

import sys
import pprint
import Parser
if len(sys.argv) != 3:  
        print 'Invalid argument count.'  
osname = sys.argv[2] 
file = sys.argv[1] 
	
parser = Parser.Parser(file)
i=0	
print '\nscan session:'

session = parser.get_session()

print "\tstart time:\t" + session.start_time
print "\tstop time:\t" + session.finish_time
print "\tnmap version:\t" + session.nmap_version
print "\tnmap args:\t" + session.scan_args
print "\ttotal hosts:\t" + session.total_hosts
print "\tup hosts:\t" + session.up_hosts
print "\tdown hosts:\t" + session.down_hosts

for h in parser.all_hosts():
	s = h.get_osname(osname)
		
	if s == None:
		print h.ip
		print "\t\t no match"

	else:
		i=i+1
		print h.ip
		print "\t\t" + s.name
print "find\t\t" +osname+":"
print i
		
			


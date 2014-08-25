#!/usr/bin/python

__author__ =  'fengxuan
__version__=  '0.2'

import sys
import xml.dom.minidom

class osmatch:
	def __init__( self, osmatch ):
		self.name = osmatch.getAttribute('name')


if __name__ == '__main__':

	dom = xml.dom.minidom.parse('result.xml')

	osmatch_nodes = dom.getElementsByTagName('osmatch')
	if len(osmatch_nodes) == 0:
		sys.exit()
	
	node = dom.getElementsByTagName('osmatch')[0]
	
	s = osmatch( node )
	print s.name


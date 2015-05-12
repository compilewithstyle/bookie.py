#!/usr/bin/env python

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#   Author:
#       Nicholas Siow
#
#   Description:
#	Enforces formatting and removes old entries for bro blackbook
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

import os
import glob
import datetime

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#
#	CONFIG PANEL - make changes here and nowhere else!
#
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

BRO_LOCAL = "/usr/local/bro/share/bro/site"

TIME_FORMAT = "%Y-%m-%d"
SEPARATOR = r'\x09'
CURRENT_FILE, CURRENT_LINE, CURRENT_LN = None, None, None

#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
#	end of config panel
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

#

###########################################################################
#	functions to make output easier
###########################################################################

def _pass(filename):
	print "[PASS]: " + filename

def _fail(filename, ln, reason):
	print "[FAIL]: file {0} failed in line {1} with the following reason:\n{2}".format(filename, ln, reason)
	exit(1)

def _info(msg):
	pass

def main():

	## find all brodata files in the local-BRO directory
	##
	brodata_files = []
	for d, _, files in os.walk(BRO_LOCAL):
		for f in files:
			path = os.path.join(d, f)
			if path.endswith('.brodata'):
				brodata_files.append(path)
	_info("Found {0} .brodata files".format(len(brodata_files)))

	if not brodata_files:
		print "Could not find any .brodata files to parse. Exiting script."
		exit(1)

	## analyze each file, checking it for correctness as well as cleaning out
	## expired entries
	##
	for f in brodata_files:
		
		lines = map(rstrip, open(f, 'r').readlines)

		##
		## check for correctness
		##

		## make sure the first line is the separator field
		expected_sep_line = EXP

		##
		## edit file
		##

	print brodata_files

	

if __name__ == '__main__':
	main()

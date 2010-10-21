#!/usr/bin/env python
import optparse
import logging
import sys
import os
import fnmatch
import subprocess
import re

def main():
	pattern=re.compile('(\\\\\[%.*?%\])', re.DOTALL)
	p = optparse.OptionParser()
	p.add_option('--person', '-p', default="world")
	options, arguments = p.parse_args()
	for root, subFolders, files in os.walk(os.environ['PROJECT_DIR']):
		for file in fnmatch.filter(files, '*.xib'):
			filename=os.path.join(root,file)
			fileout=filename+'.m'
			if ((not os.path.exists(fileout)) or (os.stat(filename).st_mtime>os.stat(fileout).st_mtime)):
				code=subprocess.Popen(['/usr/local/bin/nib2objc',filename], stdout=subprocess.PIPE).communicate()[0]
				f = open(fileout,'w')
				f.write(code)

if __name__ == '__main__':
	main()


#!/usr/bin/env python
import optparse
import logging
import sys
import os
import fnmatch
import subprocess
import re

LOG_FILENAME='/tmp/nib2objc.log'
logging.basicConfig(filename=LOG_FILENAME,level=logging.DEBUG)

def main():
	pattern=re.compile('(\\\\\[%.*?%\])', re.DOTALL)
	p = optparse.OptionParser()
	p.add_option('--person', '-p', default="world")
	options, arguments = p.parse_args()
	logging.debug('Hello %s' % arguments)
	logging.debug(os.environ['PROJECT_DIR'])
	fileList=[]
	for root, subFolders, files in os.walk(os.environ['PROJECT_DIR']):
    		for file in fnmatch.filter(files, '*.xib'):
			filename=os.path.join(root,file)
        		fileList.append(filename)
			code=subprocess.Popen(['/usr/local/bin/nib2objc',filename], stdout=subprocess.PIPE).communicate()[0]
			f = open(filename+'.m','w')
			f.write(code)
	logging.debug(fileList)

if __name__ == '__main__':
	main()


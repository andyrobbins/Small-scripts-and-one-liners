#!/usr/bin/python

import argparse
import os
import re

# Grab our argument values with ArgParse
parser = argparse.ArgumentParser(description='Sort IPs in file and kill dupes')
parser.add_argument('-f', '--file', help='The file containing unsorted IP addresses', action='store')
args = parser.parse_args()
inputFile = args.file

# Define regex for an IP address (this will match IPv4 addresses,
# but will also match things like 111.333.555.999)
r = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')

# Declare uniqueIpList as an empty dict
uniqueIpList = []

# Get the IPs out of the file and kill dupes
with open(inputFile) as file:
    ipList = file.read().split('\n')
    for line in ipList:
        if r.search(line): # Ignore anything that isn't an IP
            if line in uniqueIpList: # Ignore duplicate matches
                pass
            else:
                uniqueIpList.append(line)

#Pre-process each item, changing '192.168.1.22' into '192.168.  1. 22'
for i in range(len(uniqueIpList)):
    uniqueIpList[i] = '%3s.%3s.%3s.%3s' % tuple(uniqueIpList[i].split('.'))
    
#Sort the pre-processed list of IP addresses
uniqueIpList.sort()

#Turn the IP addresses back to 'normal' and output to our results file
for i in range(len(uniqueIpList)):
    uniqueIpList[i] = uniqueIpList[i].replace(' ','')
    with open('results.txt', 'a+') as output_file:
        output_file.write(uniqueIpList[i] + '\n')

print 'Done'
